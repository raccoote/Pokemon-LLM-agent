import time
import logging

logger = logging.getLogger(__name__)

class NPCInteractionTracker:
    """Tracks NPC interactions to prevent accidental re-triggering."""
    
    def __init__(self, interaction_timeout=5.0):
        self.last_interaction_pos = None
        self.last_interaction_time = 0.0
        self.interaction_timeout = interaction_timeout
        self.min_movement_dist = 1

    def record_interaction(self, x, y):
        """Record an interaction at the given coordinates."""
        self.last_interaction_pos = (x, y)
        self.last_interaction_time = time.time()
        logger.debug(f"Recorded NPC interaction at ({x}, {y})")

    def can_interact(self, current_x, current_y):
        """Check if we can interact again based on position and time."""
        if self.last_interaction_pos is None:
            return True

        # Check timeout
        if time.time() - self.last_interaction_time > self.interaction_timeout:
            return True

        # Check distance
        dist = abs(current_x - self.last_interaction_pos[0]) + abs(current_y - self.last_interaction_pos[1])
        if dist >= self.min_movement_dist:
            return True

        return False

    def reset(self):
        """Clear interaction history."""
        self.last_interaction_pos = None
        self.last_interaction_time = 0
