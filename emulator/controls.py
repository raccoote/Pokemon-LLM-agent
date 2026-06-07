import time
import logging
from typing import Optional
from pyboy.utils import WindowEvent

logger = logging.getLogger(__name__)

class InputManager:
    """Centralized input management without rate limiting or cooldowns."""
    def __init__(self, manager):
        self.manager = manager
        self.frame_count = 0
        
        self.button_map = {
            "up": WindowEvent.PRESS_ARROW_UP,
            "down": WindowEvent.PRESS_ARROW_DOWN,
            "left": WindowEvent.PRESS_ARROW_LEFT,
            "right": WindowEvent.PRESS_ARROW_RIGHT,
            "a": WindowEvent.PRESS_BUTTON_A,
            "b": WindowEvent.PRESS_BUTTON_B,
            "start": WindowEvent.PRESS_BUTTON_START,
            "select": WindowEvent.PRESS_BUTTON_SELECT
        }
        self.release_map = {
            "up": WindowEvent.RELEASE_ARROW_UP,
            "down": WindowEvent.RELEASE_ARROW_DOWN,
            "left": WindowEvent.RELEASE_ARROW_LEFT,
            "right": WindowEvent.RELEASE_ARROW_RIGHT,
            "a": WindowEvent.RELEASE_BUTTON_A,
            "b": WindowEvent.RELEASE_BUTTON_B,
            "start": WindowEvent.RELEASE_BUTTON_START,
            "select": WindowEvent.RELEASE_BUTTON_SELECT
        }

    def update_frame_count(self):
        self.frame_count += 1

    def press(self, button: str, hold_frames: int = 5):
        """Press and release a button immediately (no cooldown)."""
        btn = button.lower()
        if btn not in self.button_map:
            return False

        # Log action press as requested by user
        logger.info(f"[INPUT] Pressing {btn}")
        
        with self.manager.lock:
            self.manager.pyboy.send_input(self.button_map[btn])
            
        # Hold for N frames
        time.sleep(hold_frames * 0.016)
        
        with self.manager.lock:
            self.manager.pyboy.send_input(self.release_map[btn])
            
        return True

    def move(self, direction: str):
        """Move one tile."""
        if self.press(direction, hold_frames=10):
             time.sleep(10 * 0.016) # Additional wait for movement animation
             return True
        return False

    def press_start(self):
        return self.press("start")

    def press_select(self):
        return self.press("select")

    def press_a(self):
        return self.press("a")

    def press_b(self):
        return self.press("b")

    def wait(self, frames: int):
        time.sleep(frames * 0.016)

# Alias for compatibility
Controller = InputManager
