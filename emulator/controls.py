import time
import logging
from pyboy.utils import WindowEvent

logger = logging.getLogger(__name__)

from typing import Optional

class InputManager:
    """
    Centralized input management with rate limiting, cooldowns, and edge-triggering.
    """
    def __init__(self, manager):
        self.manager = manager
        self.last_press_time = {} # button -> frame_count
        self.button_states = {}   # button -> is_held
        self.frame_count = 0
        
        # Default cooldowns in frames
        self.default_cooldowns = {
            "a": 0,
            "b": 5,
            "start": 5,
            "select": 5,
            "up": 5,
            "down": 5,
            "left": 5,
            "right": 5
        }

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
        """Update internal frame counter based on emulator ticks if possible, or just increment."""
        self.frame_count += 1

    def press(self, button: str, hold_frames: int = 5, cooldown_frames: Optional[int] = None):
        """
        Press and release a button with cooldown.
        Returns True if the button was successfully pressed.
        """
        btn = button.lower()
        if btn not in self.button_map:
            return False

        current_time = self.frame_count
        last_time = self.last_press_time.get(btn, -1000)
        required_cooldown = cooldown_frames if cooldown_frames is not None else self.default_cooldowns.get(btn, 10)

        if current_time - last_time < required_cooldown:
            logger.warning(
                f"InputManager: {btn} blocked by cooldown "
                f"(frame={current_time}, last={last_time}, required={required_cooldown})"
            )
            return False

        logger.debug(f"InputManager: Pressing {btn}")
        with self.manager.lock:
            self.manager.pyboy.send_input(self.button_map[btn])
            
        # Hold for N frames
        time.sleep(hold_frames * 0.016)
        
        with self.manager.lock:
            self.manager.pyboy.send_input(self.release_map[btn])
            
        self.last_press_time[btn] = current_time
        return True

    def move(self, direction: str):
        """Move one tile."""
        if self.press(direction, hold_frames=10, cooldown_frames=15):
             time.sleep(10 * 0.016) # Additional wait for movement animation
             return True
        return False

    def press_start(self, cooldown_frames: int = 0):
        """Press START. Default cooldown=0 so startup calls are never silently blocked."""
        return self.press("start", cooldown_frames=cooldown_frames)

    def press_select(self):
        return self.press("select", cooldown_frames=30)

    def press_a(self, cooldown: Optional[int] = None):
        return self.press("a", cooldown_frames=cooldown)

    def press_b(self, cooldown: Optional[int] = None):
        return self.press("b", cooldown_frames=cooldown)

    def wait(self, frames: int):
        time.sleep(frames * 0.016)

# Alias for compatibility
Controller = InputManager

