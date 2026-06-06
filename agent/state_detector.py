import logging
from config import *
from agent.phases import GamePhase

logger = logging.getLogger(__name__)

# CF91 values observed per state
_CF91_TITLE         = 0xB0
_CF91_OAK_DIALOGUE  = 0x14
_CF91_NAME_OR_BED   = 0xA7

# CC29 values observed per state
_CC29_TITLE         = 0x00
_CC29_OAK_DIALOGUE  = 0x0B
_CC29_NAME_OR_BED   = 0xFF


class StateDetector:
    def __init__(self, manager):
        self.manager = manager

    def detect_phase(self) -> GamePhase:
        try:
            gs  = self.manager.memory.get_game_state()
            mem = self.manager.pyboy.memory

            map_id      = gs["map_id"]
            in_battle   = gs["in_battle"]
            joy_ign     = gs["joy_ignore"]
            d730        = gs["wd730"]
            party_size  = gs["party_size"]
            cf91        = mem[ADDR_CF91]
            cc29        = mem[ADDR_CC29]
            d36d        = mem[0xD36D]
            script_lock = (d730 & 0b00000010) != 0

            # 1. TITLE
            # map_id 0x00 or 0xFF = no map loaded, confirmed CF91=0xB0
            if map_id == 0 or map_id == 0xFF:
                return GamePhase.TITLE

            # 2. BATTLE
            if in_battle:
                return GamePhase.BATTLE

            # 3. DIALOGUE — joy lock, always reliable for any textbox
            if joy_ign != 0:
                return GamePhase.DIALOGUE

            # 4. OAK DIALOGUE
            # Confirmed: CF91=0x14, CC29=0x0B
            if cf91 == 0x14 and cc29 == 0x0B:
                return GamePhase.DIALOGUE

            # 5. NAME SELECTION
            # Confirmed: CF91=0xA7, CC29=0xFF, D36D=0x00 (no real map)
            if cf91 == 0xA7 and cc29 == 0xFF and d36d == 0x00:
                return GamePhase.NAME_SELECTION

            # 6. BEDROOM
            # Confirmed: CF91=0xA7, CC29=0xFF, D36D=0x3F (real map loaded)
            # Party still 0, player can move freely
            if cf91 == 0xA7 and cc29 == 0xFF and d36d != 0x00:
                return GamePhase.OVERWORLD

            # 7. MENU
            if gs["menu_state"] != 0:
                return GamePhase.MENU

            # 8. OVERWORLD
            # Must have party (real gameplay) and no script lock
            if party_size > 0 and not script_lock:
                return GamePhase.OVERWORLD

            # 9. Fallback — party=0 but no fingerprint matched
            if party_size == 0:
                return GamePhase.DIALOGUE

            return GamePhase.INTRO

        except Exception:
            logger.exception("Exception in detect_phase")
            return GamePhase.UNKNOWN

    def _textbox_active(self, mem) -> bool:
        try:
            return mem[ADDR_TEXTBOX_ID] != 0
        except Exception:
            return False

    def _joy_locked(self, mem) -> bool:
        try:
            return mem[ADDR_JOY_IGNORE] != 0
        except Exception:
            return False

    def _player_has_control(self, mem) -> bool:
        try:
            textbox     = mem[ADDR_TEXTBOX_ID]
            joy_ign     = mem[ADDR_JOY_IGNORE]
            d730        = mem[ADDR_WD730]
            script_lock = (d730 & 0b00000010) != 0
            return textbox == 0 and joy_ign == 0 and not script_lock
        except Exception:
            return False

    def detect_dialogue(self, mem=None) -> bool:
        if mem is None:
            mem = self.manager.pyboy.memory
        gs = self.manager.memory.get_game_state()
        cf91 = gs.get("cf91", 0)
        cc29 = mem[0xCC29]
        return (
            self._joy_locked(mem) or
            self._textbox_active(mem) or
            (cf91 == _CF91_OAK_DIALOGUE and cc29 == _CC29_OAK_DIALOGUE) or
            gs["party_size"] == 0
        )

    def has_player_control(self) -> bool:
        return self._player_has_control(self.manager.pyboy.memory)

    def detect_title_screen(self) -> bool:
        map_id = self.manager.memory.get_game_state().get("map_id", 0)
        return map_id == 0 or map_id == 0xFF

    def detect_intro_scene(self) -> bool:
        mem = self.manager.pyboy.memory
        return self.detect_dialogue(mem) and not self._player_has_control(mem)

    def detect_overworld(self) -> bool:
        gs = self.manager.memory.get_game_state()
        return (
            self._player_has_control(self.manager.pyboy.memory) and
            gs["party_size"] > 0
        )