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
    navigate_to,
    navigate_around
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
            navigate_to,
            navigate_around
            # save_state,
            # load_state
        ]

        # Load system instructions from file (everything is now in here)
        prompt_path = Path(__file__).parent / "system_prompt.txt"
        self.instructions = prompt_path.read_text().strip()

        # ToolCallingAgent does NOT accept system_prompt in constructor for this version
        # We will continue to prepend it to the run() call to be safe with this version 
        # but keep it all consolidated in system_prompt.txt
        self.agent = ToolCallingAgent(
            tools=self.tools,
            model=self.model,
            max_steps=6
        )

    def get_next_goal(self, state, phase, history, logic_note):
        # Full instructions from system_prompt.txt + dynamic session data
        prompt = f"""
{self.instructions}

CURRENT SESSION DATA:
- PHASE: {phase}
- STATE: {state}
- HISTORY: {history}
- LOGIC NOTE: {logic_note}
"""
        
        logger.info("=" * 60)
        logger.info("[LLM REQUEST SENT]")
        logger.info(prompt.strip())
        logger.info("=" * 60)

        try:
            response = self.agent.run(prompt)
            # If agent.run returns the final result, we parse it.
            # If it failed or returned raw text, we handle it gracefully.
            cleaned = str(response).strip()

            # extract JSON safely (finding the last JSON-like block in case of chatter)
            matches = list(re.finditer(r"\{.*\}", cleaned, re.DOTALL))
            
            logger.info(f"[LLM RAW RESPONSE]: {cleaned}")

            if not matches:
                logger.error(f"No JSON found in LLM output.")
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
                
                logger.info("\n" + "="*20 + " [LLM THINKING] " + "="*20)
                logger.info(f"Reasoning: {analysis}")
                logger.info(f"Decision: {goal}")
                logger.info(f"Target: {action.get('target_location')}")
                logger.info("=" * 60 + "\n")

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