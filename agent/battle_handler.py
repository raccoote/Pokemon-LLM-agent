import logging
import time

logger = logging.getLogger(__name__)

def handle_battle_phase(manager):
    """Handle the battle phase."""
    logger.info("Entering battle phase logic")
    # For now, we still use the primitive spam A strategy
    while manager.memory.is_in_battle():
        manager.controls.press_a()
        time.sleep(0.1)
    logger.info("Battle finished")
