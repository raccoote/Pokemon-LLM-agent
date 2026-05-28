import logging
from agent.phases import GamePhase

logger = logging.getLogger(__name__)

def handle_menu(manager):
    """Handle menu interactions (deterministic or basic for now)."""
    logger.info("Menu detected, attempting to clear or navigate")
    # Basic logic: if stuck in menu, try to exit with B unless we have a reason to be there
    # For now, let's just press B to get back to game if the agent didn't intentionally open it
    manager.controls.press_b()
