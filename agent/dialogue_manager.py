import logging
import time
from enum import Enum, auto
import config
from agent.npc_interaction_tracker import NPCInteractionTracker
from agent.interaction_cooldown import InteractionCooldown

logger = logging.getLogger(__name__)

class DialogueState(Enum):
    PLAYER_CONTROL_RETURNED = auto()
    DIALOGUE_ACTIVE = auto()
    DIALOGUE_ENDING = auto()

class DialogueManager:
    """Robust lifecycle handling for dialogue."""
    
    def __init__(self, manager):
        self.manager = manager
        self.state = DialogueState.PLAYER_CONTROL_RETURNED
        self.tracker = NPCInteractionTracker()
        self.cooldown = InteractionCooldown(cooldown_duration=1.5)
        
        self.consecutive_a_presses = 0
        self.max_a_presses = 50 
        self.last_press_frame = 0

    def can_interact(self, ram_state):
        """Check if an NPC interaction is allowed."""
        if self.state != DialogueState.PLAYER_CONTROL_RETURNED:
            return False
        if self.cooldown.check():
            return False
        return True

    def update(self, ram_state):
        """Update dialogue state machine."""
        # Use common detection logic from StateDetector if possible,
        # but here we use a local check for simplicity or specific nuances.
        is_dialogue = self._detect_dialogue_ram(ram_state)
        
        if self.state == DialogueState.PLAYER_CONTROL_RETURNED:
            if is_dialogue:
                logger.info("Dialogue detected (Phase: Started)")
                self.state = DialogueState.DIALOGUE_ACTIVE
                self.consecutive_a_presses = 0

        elif self.state == DialogueState.DIALOGUE_ACTIVE:
            if not is_dialogue:
                logger.info("Dialogue ended (Phase: Ending)")
                self.state = DialogueState.DIALOGUE_ENDING
                self.cooldown.start()

        elif self.state == DialogueState.DIALOGUE_ENDING:
            if not self.cooldown.check():
                self.state = DialogueState.PLAYER_CONTROL_RETURNED

    def handle_dialogue(self):
        """Active handling of dialogue with rate limiting."""
        if not self._detect_dialogue_ram(self.manager.memory.get_game_state()):
            return

        # Use InputManager's internal frame count for cooldown
        current_frame = self.manager.controls.frame_count
        if current_frame - self.last_press_frame < 30: # 30 frame cooldown (~0.5s)
            return

        logger.info(f"Progressing dialogue (A press {self.consecutive_a_presses + 1})")
        if self.manager.controls.press_a(cooldown=20):
            self.last_press_frame = current_frame
            self.consecutive_a_presses += 1

    def handle_intro_dialogue(self):
        """Dedicated intro dialogue handler (like Professor Oak)."""
        # Intro dialogue is more sensitive, we wait longer
        ram = self.manager.memory.get_game_state()
        if not self._detect_dialogue_ram(ram):
            return

        current_frame = self.manager.controls.frame_count
        if current_frame - self.last_press_frame < 40: # 40 frame wait
            return

        logger.info("Handling intro dialogue press...")
        if self.manager.controls.press_a(cooldown=30):
            self.last_press_frame = current_frame

    def _detect_dialogue_ram(self, ram_state) -> bool:
        """Heuristic for dialogue/textbox presence."""
        with self.manager.lock:
            ram = self.manager.pyboy.memory
            status_flags = ram[config.ADDR_WD730]
            text_id = ram[config.ADDR_TEXTBOX_ID]
            joy_ignore = ram[config.ADDR_JOY_IGNORE]
            # Extra check: 0xD358 often non-zero when textbox is open
            textbox_open = ram[0xD358] > 0
            
        in_dialogue = (status_flags & 0x20) > 0
        movement_locked = (status_flags & 0x10) > 0
        
        return text_id > 0 and (in_dialogue or movement_locked or joy_ignore > 0 or textbox_open)

