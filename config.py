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
LLM_MODEL = "qwen3.5-2b"
LM_STUDIO_BASE_URL = "http://localhost:1234/v1"

# Action Thresholds
MAX_STEPS_PER_GOAL = 100
LOOP_DETECTION_THRESHOLD = 5 # Number of times in same position before flagging loop
