import json
import logging
import re
from pathlib import Path

import config
from smolagents import ToolCallingAgent, OpenAIServerModel

from tools.pokemon_tools import (
    move_up,
    move_down,
    move_left,
    move_right,
    press_a,
    press_b,
    press_start,
    press_select,
    navigate_to
    # save_state,
    # load_state
)

logger = logging.getLogger(__name__)


class Planner:
    def __init__(self):
        self.model = OpenAIServerModel(
            model_id=config.LLM_MODEL,
            api_base=config.LM_STUDIO_BASE_URL,
            api_key="lm-studio"
        )

        # Tools available to model (simplified)
        self.tools = [
            move_up,
            move_down,
            move_left,
            move_right,
            press_a,
            press_b,
            press_start,
            press_select,
            navigate_to
            # save_state,
            # load_state
        ]

        # Load system instructions from file
        prompt_path = Path(__file__).parent / "system_prompt.txt"
        self.instructions = prompt_path.read_text().strip()

        self.format_rules = """
CRITICAL OUTPUT FORMAT RULE:
You MUST output ONLY valid JSON.
Never output plain text outside the JSON structure.

Required format:
{
  "goal": "explore|navigate",
  "analysis": "detailed reasoning of your visual observation and strategy",
  "target_location": {"x": int, "y": int} or null
}
"""

        # ToolCallingAgent does NOT accept system_prompt in constructor for this version
        self.agent = ToolCallingAgent(
            tools=self.tools,
            model=self.model,
            max_steps=3
        )

    def get_next_goal(self, state, phase, history, logic_note):
        # We include instructions in the prompt because smolagents ToolCallingAgent 
        # is stateless across .run() calls in this implementation.
        prompt = f"""
{self.instructions}

{self.format_rules}

CURRENT SESSION DATA:
- PHASE: {phase}
- STATE: {state}
- HISTORY: {history}
- LOGIC NOTE: {logic_note}

Task:
1. Analyze the current state.
2. Use your tools (up to 3 steps) to perform necessary actions (moving, talking, etc.).
3. Once finished, provide your final conclusion using the JSON format specified above.
"""

        try:
            response = self.agent.run(prompt)
            # If agent.run returns the final result, we parse it.
            # If it failed or returned raw text, we handle it gracefully.
            cleaned = str(response).strip()

            # extract JSON safely (finding the last JSON-like block in case of chatter)
            matches = list(re.finditer(r"\{.*\}", cleaned, re.DOTALL))
            
            if not matches:
                logger.error(f"No JSON found in LLM output. Raw response: {cleaned}")
                # Use the raw response as analysis so the user/agent can see what happened
                return {
                    "goal": "explore",
                    "analysis": cleaned if cleaned else "Model returned no text",
                    "target_location": None
                }

            # Use the last match which is usually the intended JSON
            match = matches[-1]
            try:
                action = json.loads(match.group())
                
                # High-visibility reasoning log
                analysis = action.get("analysis", "No reasoning provided")
                goal = action.get("goal", "explore")
                logger.info(f"\n[LLM THINKING]\nReasoning: {analysis}\nDecision: {goal}\n")

                return {
                    "goal": goal,
                    "analysis": analysis,
                    "target_location": action.get("target_location", None)
                }

            except Exception as e:
                logger.error(f"JSON parse failed for: {cleaned}")
                return {
                    "goal": "explore",
                    "analysis": f"(Partial/Invalid JSON) {cleaned[:300]}...",
                    "target_location": None
                }

        except Exception as e:
            logger.error(f"Planner execution failed: {e}")
            return {
                "goal": "explore",
                "analysis": f"Execution Error: {str(e)}",
                "target_location": None
            }
    