import logging
from .menus import close_all_menus

logger = logging.getLogger(__name__)

def recovery_mode(manager):
    """
    Called when the agent is stuck or looping.
    Attempts to get back to a clean state.
    """
    logger.info("Entering recovery mode...")
    close_all_menus(manager)
    # Move randomly for a few steps
    for _ in range(5):
        import random
        dir = random.choice(["up", "down", "left", "right"])
        manager.controls.move(dir)
    logger.info("Recovery complete.")
    return True
