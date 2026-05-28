import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
ROM_PATH = BASE_DIR / "pokemon_red.gb"
SAVE_DIR = BASE_DIR / "saves"
LOG_DIR = BASE_DIR / "logs"

# Ensure directories exist
SAVE_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# Emulator Settings
HEADLESS = False  # Set to True for faster execution
SPEED = 1         # 0 for max speed, 1 for real-time
SOUND_ENABLED = True
WINDOW_SCALE = 3

# LLM Settings
LLM_MODEL = "qwen2.5-3b-instruct"
LM_STUDIO_BASE_URL = "http://localhost:1234/v1"

# RAM Addresses (Pokemon Red US)
# Source: https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_Red_and_Blue/RAM_map
#         + pret/pokered disassembly (pokered.sym)
ADDR_PLAYER_X       = 0xD362  # wXCoord
ADDR_PLAYER_Y       = 0xD361  # wYCoord
ADDR_MAP_ID         = 0xD35E  # wCurMap (0 / 0xFF = no map loaded yet)
ADDR_PARTY_SIZE     = 0xD163  # wPartyCount: 0 = no Pokémon yet
ADDR_PARTY_HP       = 0xD16C  # wPartyMon1HP (start of party HP data)
ADDR_IS_IN_BATTLE   = 0xD057  # wIsInBattle: 0=no, 1=wild, 2=trainer
ADDR_IN_BATTLE      = 0xD057  # alias
ADDR_MENU_STATE     = 0xD057  # (reused – battle flag doubles as chief state)
ADDR_TEXTBOX_ID     = 0xCF13  # wTextBoxID: non-zero = any textbox active
ADDR_JOY_IGNORE     = 0xCD6B  # wJoyIgnore: non-zero = input locked (dialogue/cutscene)
ADDR_WD730          = 0xD730  # bit 1 = scripted movement lock
ADDR_PLAYER_NAME    = 0xD158  # wPlayerName byte 1: 0x50 = empty/terminator
ADDR_CF91           = 0xCF91  # Script engine state: 0x14=Oak dialogue, 0xA7=name/bedroom
ADDR_CC29           = 0xCC29  # Joy bitmask: 0x0B=Oak dialogue, 0xFF=name selection/bedroom
ADDR_D36D           = 0xD36D  # Map script pointer: 0x00 = no real map, nonzero = real map active

# Action Thresholds
MAX_STEPS_PER_GOAL = 100
LOOP_DETECTION_THRESHOLD = 5 # Number of times in same position before flagging loop
