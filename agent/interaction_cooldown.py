import time
import logging

logger = logging.getLogger(__name__)

class InteractionCooldown:
    """Manages cooldowns after significant events like dialogue completion."""
    
    def __init__(self, cooldown_duration=1.0):
        self.cooldown_end_time = 0.0
        self.cooldown_duration = cooldown_duration
        self.is_active = False

    def start(self, duration=None):
        """Start a cooldown period."""
        d = duration if duration is not None else self.cooldown_duration
        self.cooldown_end_time = time.time() + d
        self.is_active = True
        logger.debug(f"Interaction cooldown started for {d}s")

    def check(self):
        """Check if we are currently in cooldown."""
        if not self.is_active:
            return False
            
        if time.time() > self.cooldown_end_time:
            self.is_active = False
            return False
            
        return True

    def remaining(self):
        """Return remaining cooldown time."""
        return max(0, self.cooldown_end_time - time.time())
