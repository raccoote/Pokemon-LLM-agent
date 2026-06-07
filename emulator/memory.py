import logging
import json
from pathlib import Path
from config import *

logger = logging.getLogger(__name__)

class MemoryReader:
    def __init__(self, manager):
        self.manager = manager
        self.pyboy = manager.pyboy
        self.addresses = self._load_addresses()

    def _load_addresses(self):
        """Load RAM addresses from external JSON."""
        json_path = Path(__file__).parent.parent / "constants" / "ram_addresses.json"
        with open(json_path, "r") as f:
            return json.load(f)

    def get_addr(self, path):
        """Get integer address from path like 'player.x'."""
        parts = path.split('.')
        val = self.addresses
        for p in parts:
            if isinstance(val, dict) and p in val:
                val = val[p]
            else:
                raise KeyError(f"Address path '{path}' not found in RAM JSON.")
        
        if isinstance(val, str):
            return int(val, 16)
        return val

    def get_player_pos(self):
        with self.manager.lock:
            x = self.manager.pyboy.memory[self.get_addr("player.x")]
            y = self.manager.pyboy.memory[self.get_addr("player.y")]
        return x, y

    def get_map_id(self):
        with self.manager.lock:
            return self.manager.pyboy.memory[self.get_addr("player.map_id")]

    def is_in_battle(self):
        with self.manager.lock:
            return self.manager.pyboy.memory[self.get_addr("battle.in_battle")] > 0

    def get_party_info(self):
        with self.manager.lock:
            count = self.manager.pyboy.memory[self.get_addr("party.count")]
            party = []
            for i in range(count):
                hp_start = self.get_addr("party.mon1_hp") + (i * 44)
                current_hp = (
                    (self.manager.pyboy.memory[hp_start] << 8) |
                    self.manager.pyboy.memory[hp_start + 1]
                )
                party.append({"id": i, "hp": current_hp})
            return party

    def get_game_state(self):
        with self.manager.lock:
            mem = self.manager.pyboy.memory

            party_size  = mem[self.get_addr("party.count")]
            player_name = mem[self.get_addr("player.name")]  # 0x50 = terminator = unset
            name_unset  = player_name == 0x00 or player_name == 0x50
            map_id      = mem[self.get_addr("player.map_id")]

            return {
                # Position
                "player_x":    mem[self.get_addr("player.x")],
                "player_y":    mem[self.get_addr("player.y")],

                # Map / battle
                "map_id":      map_id,
                "in_battle":   mem[self.get_addr("battle.in_battle")] > 0,

                # Party
                "party":       self.get_party_info(),
                "party_size":  party_size,

                # Dialogue / input lock signals
                "textbox":     mem[self.get_addr("ui.textbox_id")],    # 0xCF13
                "joy_ignore":  mem[self.get_addr("ui.joy_ignore")],    # 0xCD6B
                "wd730":       mem[self.get_addr("engine.wd730")],         # 0xD730
                "cf91":        mem[self.get_addr("engine.cf91")],          # 0xCF91
                "cc29":        mem[self.get_addr("engine.cc29")],          # 0xCC29

                # Menu
                "menu_state":  mem[self.get_addr("ui.current_menu_item")],             # wCurrentMenuItem

                # Pre-game fingerprint
                "player_name_byte": player_name,        # 0x50 or 0x00 = unset
                "is_pregame":  party_size == 0 and name_unset and map_id != 0,
            }