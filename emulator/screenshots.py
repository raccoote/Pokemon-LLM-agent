import os
from PIL import Image
import logging

logger = logging.getLogger(__name__)

class ScreenshotHandler:
    def __init__(self, manager):
        self.manager = manager
        # Backwards compatibility
        self.pyboy = manager.pyboy

    def capture(self, filename="last_frame.png"):
        """Captures the current screen and saves it."""
        try:
            with self.manager.lock:
                screen = self.manager.pyboy.screen_image()
            
            if screen:
                screen.save(filename)
                return filename
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {e}")
        return None

    def get_rgb_array(self):
        """Returns the screen as a numpy array."""
        import numpy as np
        with self.manager.lock:
            img = self.manager.pyboy.screen_image()
        return np.array(img)
