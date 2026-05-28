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

            # if self.detector.detect_dialogue(self.manager.pyboy.memory):

            #     logger.info("Dialogue detected in overworld -> pressing A")

            #     self.manager.controls.handle_dialogue()

            #     return

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
        """Log raw values of key RAM addresses once per second (every 10 iters)."""
        try:
            with self.manager.lock:
                mem = self.manager.pyboy.memory
                textbox    = mem[ADDR_TEXTBOX_ID]   # 0xCF13
                joy_ignore = mem[ADDR_JOY_IGNORE]   # 0xCD6B
                wd730      = mem[ADDR_WD730]         # 0xD730
                map_id     = mem[ADDR_MAP_ID]        # 0xD35E
                in_battle  = mem[ADDR_IN_BATTLE]     # 0xD057
                party_size = mem[ADDR_PARTY_SIZE]    # 0xD163
                plr_name   = mem[ADDR_PLAYER_NAME]   # 0xD158
                script_lock = (wd730 & 0b00000010) != 0

            # logger.info(
            #     f"[RAM] "
            #     f"textbox=0x{mem[ADDR_TEXTBOX_ID]:02X}  "
            #     f"joy_ign=0x{mem[ADDR_JOY_IGNORE]:02X}  "
            #     f"wd730=0x{mem[ADDR_WD730]:02X}  "
            #     f"map=0x{mem[ADDR_MAP_ID]:02X}({mem[ADDR_MAP_ID]})  "
            #     f"battle={mem[ADDR_IS_IN_BATTLE]}  "
            #     f"party={mem[ADDR_PARTY_SIZE]}  "
            #     f"plr_name=0x{mem[ADDR_PLAYER_NAME]:02X}  "
            #     f"cf91=0x{mem[ADDR_CF91]:02X}  "
            #     f"cc29=0x{mem[ADDR_CC29]:02X}"
            # )
            # logger.info(
            #     f"[PARTY] "
            #     f"size={mem[ADDR_PARTY_SIZE]}  "
            #     f"mon1=0x{mem[0xD164]:02X}  "   # first party slot pokemon ID
            #     f"mon1_hp={mem[0xD16C]:02X}{mem[0xD16D]:02X}  "  # mon1 current HP (2 bytes)
            #     f"mon1_lvl=0x{mem[0xD18C]:02X}"  # mon1 actual level
            # )
            # logger.info(
            #     f"[PHASE_SIGNALS] "
            #     f"script_lock={(mem[ADDR_WD730] & 0b00000010) != 0}  "
            #     f"name_unset={mem[ADDR_PLAYER_NAME] in (0x00, 0x50)}  "
            #     f"is_pregame={mem[ADDR_PARTY_SIZE] == 0 and mem[ADDR_MAP_ID] not in (0x00, 0xFF)}  "
            #     f"would_be_overworld={mem[ADDR_PARTY_SIZE] > 0 and mem[ADDR_IS_IN_BATTLE] == 0 and mem[ADDR_JOY_IGNORE] == 0}"
            # )
            logger.info(
                f"[MOVE DEBUG] "
                f"player_x={mem[ADDR_PLAYER_X]}  "
                f"player_y={mem[ADDR_PLAYER_Y]}  "
                f"D36D={mem[0xD36D]:02X}  "   # map script pointer
                # f"D736={mem[0xD736]:02X}  "
                # f"D72E={mem[0xD72E]:02X}  "
                # f"C0EF={mem[0xC0EF]:02X}  "   # audio bank (changes between screens)
                # f"FF9F={mem[0xFF9F]:02X}  "   # HRAM money/coins
                # f"D364={mem[0xD364]:02X}  "   # player X block position
                # f"D363={mem[0xD363]:02X}  "   # player Y block position
                # f"D35F={mem[0xD35F]:02X}  "   # event displacement
                # f"D360={mem[0xD360]:02X}  "   # event displacement 2
            )

        except Exception:
            logger.exception("Exception in _log_ram_state")

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