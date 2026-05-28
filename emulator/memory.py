import logging
from config import *

logger = logging.getLogger(__name__)

class MemoryReader:
    def __init__(self, manager):
        self.manager = manager
        self.pyboy = manager.pyboy

    def get_player_pos(self):
        with self.manager.lock:
            x = self.manager.pyboy.memory[ADDR_PLAYER_X]
            y = self.manager.pyboy.memory[ADDR_PLAYER_Y]
        return x, y

    def get_map_id(self):
        with self.manager.lock:
            return self.manager.pyboy.memory[ADDR_MAP_ID]

    def is_in_battle(self):
        with self.manager.lock:
            return self.manager.pyboy.memory[ADDR_IS_IN_BATTLE] > 0

    def get_party_info(self):
        with self.manager.lock:
            count = self.manager.pyboy.memory[ADDR_PARTY_SIZE]
            party = []
            for i in range(count):
                hp_start = ADDR_PARTY_HP + (i * 44)
                current_hp = (
                    (self.manager.pyboy.memory[hp_start] << 8) |
                    self.manager.pyboy.memory[hp_start + 1]
                )
                party.append({"id": i, "hp": current_hp})
            return party

    def get_game_state(self):
        with self.manager.lock:
            mem = self.manager.pyboy.memory

            party_size  = mem[ADDR_PARTY_SIZE]
            player_name = mem[ADDR_PLAYER_NAME]  # 0x50 = terminator = unset
            name_unset  = player_name == 0x00 or player_name == 0x50
            map_id      = mem[ADDR_MAP_ID]

            return {
                # Position
                "player_x":    mem[ADDR_PLAYER_X],
                "player_y":    mem[ADDR_PLAYER_Y],

                # Map / battle
                "map_id":      map_id,
                "in_battle":   mem[ADDR_IS_IN_BATTLE] > 0,

                # Party
                "party":       self.get_party_info(),
                "party_size":  party_size,

                # Dialogue / input lock signals
                "textbox":     mem[ADDR_TEXTBOX_ID],    # 0xCF13
                "joy_ignore":  mem[ADDR_JOY_IGNORE],    # 0xCD6B
                "wd730":       mem[ADDR_WD730],         # 0xD730
                "cf91":        mem[ADDR_CF91],          # 0xCF91
                "cc29":        mem[ADDR_CC29],          # 0xCC29

                # Menu
                "menu_state":  mem[0xCC26],             # wCurrentMenuItem

                # Pre-game fingerprint
                "player_name_byte": player_name,        # 0x50 or 0x00 = unset
                "is_pregame":  party_size == 0 and name_unset and map_id != 0,
            }