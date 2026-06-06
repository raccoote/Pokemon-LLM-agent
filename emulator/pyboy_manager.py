import logging
import threading
from pathlib import Path

from pyboy import PyBoy
import config

from .memory import MemoryReader
from .controls import Controller
from .screenshots import ScreenshotHandler

logger = logging.getLogger(__name__)

class EmulatorManager:
    def __init__(self):
        rom_path = Path(config.ROM_PATH)

        if not rom_path.exists():
            raise FileNotFoundError(f"ROM not found at: {rom_path}")

        logger.info(f"Loading ROM: {rom_path}")

        window_mode = "null" if config.HEADLESS else "SDL2"
        logger.info(f"Initializing PyBoy | window={window_mode}")

        self.pyboy = PyBoy(
            str(rom_path),
            window=window_mode,
            sound_emulated=config.SOUND_ENABLED,
        )
        self.pyboy.set_emulation_speed(config.SPEED)

        # Shared lock between Main Thread (rendering) and Agent Thread (logic/RAM/input)
        self.lock = threading.RLock()

        self.memory = MemoryReader(self)
        self.controls = Controller(self)
        self.screen = ScreenshotHandler(self)

        logger.info("PyBoy initialized successfully")

    def step(self, frames: int = 1):
        """
        Advance emulator by N frames (Safe for multi-threaded use).
        """
        with self.lock:
            for _ in range(frames):
                self.pyboy.tick()

    def save_state(self, slot: int = 1):
        save_dir = Path("saves")
        save_dir.mkdir(exist_ok=True)
        state_path = save_dir / f"state_{slot}.state"

        try:
            with self.lock:
                with open(state_path, "wb") as f:
                    self.pyboy.save_state(f)
            logger.info(f"Saved state: {state_path}")
        except Exception:
            logger.exception("Failed to save state")

    def load_state(self, slot: int = 1):
        state_path = Path("saves") / f"state_{slot}.state"
        if not state_path.exists():
            return

        try:
            with self.lock:
                with open(state_path, "rb") as f:
                    self.pyboy.load_state(f)
            logger.info(f"Loaded state: {state_path}")
        except Exception:
            logger.exception("Failed to load state")

    def capture_screen(self, path="logs/latest_frame.png"):
        try:
            with self.lock:
                self.screen.capture(path)
        except Exception:
            logger.exception("Screenshot capture failed")

    def stop(self):
        logger.info("Stopping PyBoy")
        try:
            with self.lock:
                self.pyboy.stop()
        except Exception:
            logger.exception("Failed to stop PyBoy cleanly")