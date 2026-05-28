import logging

logger = logging.getLogger(__name__)

def handle_battle(manager):
    """
    Primitive battle skill. Spams A to get through it.
    TODO: Add smarter move selection based on RAM data.
    """
    logger.info("Handling battle...")
    # Checking if still in battle
    while manager.memory.is_in_battle():
        # Press A to progress through dialog/menus
        manager.controls.press("a", ticks=10)
        manager.controls.wait(10)
        # Randomly press down sometimes to select other moves if A is stuck
        # Or just keep it simple for now
    logger.info("Battle over.")
    return True
