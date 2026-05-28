import json
import logging
import re
from pathlib import Path

import config
from smolagents import ToolCallingAgent, OpenAIServerModel

from tools.pokemon_tools import (
    get_game_state,
    move_up,
    move_down,
    move_left,
    move_right,
    press_a,
    press_b,
    press_start,
    press_select,
    navigate_to,
    save_state,
    load_state,
    take_screenshot,
    detect_phase,
    detect_dialogue,
    detect_title_screen,
    detect_intro_scene,
    detect_overworld
)

logger = logging.getLogger(__name__)


class Planner:
    def __init__(self):
        self.model = OpenAIServerModel(
            model_id=config.LLM_MODEL,
            api_base=config.LM_STUDIO_BASE_URL,
            api_key="lm-studio"
        )

        # ALL tools available to model (important fix)
        self.tools = [
            get_game_state,
            move_up,
            move_down,
            move_left,
            move_right,
            press_a,
            press_b,
            press_start,
            press_select,
            navigate_to,
            save_state,
            load_state,
            take_screenshot,
            detect_phase,
            detect_dialogue,
            detect_title_screen,
            detect_intro_scene,
            detect_overworld
        ]

        self.system_prompt = """
You are a Pokémon Red autonomous agent.

CRITICAL OUTPUT FORMAT RULE:
You MUST output ONLY valid JSON.

Never output plain text like "explore".
Never output markdown.

Required format:
{
  "goal": "explore|navigate|talk|battle|heal|recover",
  "analysis": "short reasoning of what you observed",
  "target_location": {"x": int, "y": int} or null
}

If unsure, default to:
{"goal":"explore","analysis":"uncertain state","target_location":null}
"""

        self.agent = ToolCallingAgent(
            tools=self.tools,
            model=self.model,
        )

    def get_next_goal(self, state, history, logic_note):
        prompt = f"""
CURRENT GAME STATE:
{state}

RECENT HISTORY:
{history}

LOGIC NOTE:
{logic_note}

You MUST decide next action.

IMPORTANT:
- Output ONLY JSON
- No extra text
- No markdown
"""

        try:
            response = self.agent.run(prompt)
            cleaned = str(response).strip()

            # extract JSON safely
            match = re.search(r"\{.*\}", cleaned, re.DOTALL)

            if not match:
                logger.error(f"No JSON found: {cleaned}")
                return {
                    "goal": "explore",
                    "analysis": "Invalid model output (no JSON detected)",
                    "target_location": None
                }

            try:
                action = json.loads(match.group())

                return {
                    "goal": action.get("goal", "explore"),
                    "analysis": action.get("analysis", ""),
                    "target_location": action.get("target_location", None)
                }

            except Exception as e:
                logger.error(f"JSON parse failed: {cleaned}")
                return {
                    "goal": "explore",
                    "analysis": f"Parse error: {str(e)}",
                    "target_location": None
                }

        except Exception as e:
            logger.error(f"Planner crash: {e}")
            return {
                "goal": "explore",
                "analysis": f"Exception: {str(e)}",
                "target_location": None
            }
    