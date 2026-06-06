import collections
import logging

logger = logging.getLogger(__name__)

class MemoryStore:
    def __init__(self, max_history=10, loop_threshold=5):
        self.history = collections.deque(maxlen=max_history)
        self.pos_history = collections.deque(maxlen=20)
        self.loop_threshold = loop_threshold

    def add_entry(self, state, action):
        entry = {
            "state": state,
            "action": action
        }
        self.history.append(entry)
        
        pos = (state.get("player_x"), state.get("player_y"), state.get("map_id"))
        self.pos_history.append(pos)

    def is_looping(self):
        if len(self.pos_history) < self.loop_threshold:
            return False
        
        # Simple loop detection: check if we've been in the same spot many times recently
        pos_counts = collections.Counter(self.pos_history)
        most_common = pos_counts.most_common(1)
        if most_common and most_common[0][1] >= self.loop_threshold:
            return True
        return False

    def get_history_summary(self):
        return list(self.history)[-1:] if self.history else []
