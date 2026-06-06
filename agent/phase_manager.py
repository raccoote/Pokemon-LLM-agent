import logging
import time
import random

from config import *

from agent.phases import GamePhase
from agent.state_detector import StateDetector
from agent.startup_sequence import handle_startup
from agent.battle_handler import handle_battle_phase
from agent.overworld_agent import OverworldAgent
from agent.dialogue_manager import DialogueManager

logger = logging.getLogger(__name__)


class PhaseManager:
    def __init__(self, manager, memory):
        self.manager = manager
        self.memory = memory

        self.detector = StateDetector(manager)
        self.overworld_agent = OverworldAgent()
        self.dialogue_manager = DialogueManager(manager)

        self.last_phase = None

        self.stuck_counter = 0
        self.last_state_hash = None
        self._iter = 0

    # =========================================================
    # MAIN LOOP
    # =========================================================

    def run_iteration(self):

        self.manager.controls.update_frame_count()
        self._iter += 1

        if self._iter % 10 == 0:
            self._log_ram_state()

        phase = self.detector.detect_phase()

        if phase != self.last_phase:
            logger.info(f"PHASE TRANSITION: {self.last_phase} -> {phase}")

            self.last_phase = phase
            self.stuck_counter = 0
            self.last_state_hash = None

        # -----------------------------------------------------
        # UPDATE DIALOGUE MANAGER
        # -----------------------------------------------------

        ram_state = self.manager.memory.get_game_state()

        self.dialogue_manager.update(ram_state)

        # -----------------------------------------------------
        # STUCK DETECTION ONLY IN OVERWORLD
        # -----------------------------------------------------

        if phase == GamePhase.OVERWORLD:
            if self._is_stuck():
                self._handle_stuck()
                return
        else:
            self.stuck_counter = 0

        # -----------------------------------------------------
        # STARTUP / INTRO
        # -----------------------------------------------------

        if phase in [
            GamePhase.BOOT,
            GamePhase.TITLE,
            GamePhase.INTRO,
            GamePhase.MENU,
            GamePhase.DIALOGUE,
            GamePhase.NAME_SELECTION,
            GamePhase.BEDROOM
        ]:

            handle_startup(
                self.manager,
                phase,
                self.dialogue_manager
            )

            return

        # -----------------------------------------------------
        # BATTLE
        # -----------------------------------------------------

        if phase == GamePhase.BATTLE:
            handle_battle_phase(self.manager)
            return

        # -----------------------------------------------------
        # OVERWORLD
        # -----------------------------------------------------

        if phase == GamePhase.OVERWORLD or phase == GamePhase.BEDROOM:

            self._log_ram_state()  # always log RAM before LLM planning

            action = self.overworld_agent.step(
                self.manager,
                self.memory,
                ram_state
            )

            self._execute_overworld_action(action, ram_state)

            return

        logger.warning(f"Unknown phase: {phase}")

    # =========================================================
    # RAM DIAGNOSTICS
    # =========================================================

    def _log_ram_state(self):
        """Log key RAM values occasionally."""
        try:
            with self.manager.lock:
                mem = self.manager.pyboy.memory
                logger.info(
                    f"[RAM] "
                    f"map={mem[ADDR_MAP_ID]:02X}  "
                    f"pos=({mem[ADDR_PLAYER_X]},{mem[ADDR_PLAYER_Y]})  "
                    f"battle={mem[ADDR_IS_IN_BATTLE]}  "
                    f"party={mem[ADDR_PARTY_SIZE]}"
                )
        except Exception as e:
            logger.error(f"Failed to log RAM state: {e}")

    # =========================================================
    # STUCK DETECTION
    # =========================================================

    def _is_stuck(self):

        state = self.manager.memory.get_game_state()

        state_hash = (
            state.get("player_x"),
            state.get("player_y"),
            state.get("map_id"),
            state.get("menu_state"),
        )

        if state_hash == self.last_state_hash:
            self.stuck_counter += 1
        else:
            self.stuck_counter = 0
            self.last_state_hash = state_hash

        return self.stuck_counter >= 15

    def _handle_stuck(self):

        logger.warning(
            f"Agent stuck ({self.stuck_counter}) -> recovery"
        )

        self.manager.controls.press_b()

        time.sleep(0.5)

        self.manager.controls.press_a()

        time.sleep(0.5)

        move = random.choice([
            "up",
            "down",
            "left",
            "right"
        ])

        logger.info(f"Recovery movement: {move}")

        self.manager.controls.move(move)

        self.stuck_counter = 0

    # =========================================================
    # OVERWORLD EXECUTION
    # =========================================================

    def _execute_overworld_action(self, action, state):

        from skills.navigation import (
            navigate_to,
            explore_randomly
        )

        goal = action.get("goal", "explore")
        target = action.get("target_location")

        logger.info(f"OVERWORLD ACTION: {goal}")

        try:

            if goal == "navigate" and target:

                x = target.get("x")
                y = target.get("y")

                if x is not None and y is not None:
                    navigate_to(self.manager, x, y)
                else:
                    explore_randomly(self.manager)

            elif goal == "explore":
                explore_randomly(self.manager)

            elif goal == "talk":
                self.manager.controls.press_a()

            else:
                explore_randomly(self.manager)

            self.memory.add_entry(state, action)

        except Exception:
            logger.exception("Failed executing action")