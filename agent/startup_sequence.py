import logging
import time

from agent.phases import GamePhase

logger = logging.getLogger(__name__)


def handle_startup(manager, phase, dialogue_manager):
    logger.info(f"Startup Handler: Processing {phase}")

    if phase == GamePhase.TITLE:

        manager.controls.press_start()
        time.sleep(1.0)
        return

    if phase == GamePhase.MENU:

        manager.controls.press_a()
        time.sleep(0.8)
        return

    if phase in [
        GamePhase.INTRO,
        GamePhase.DIALOGUE,
        GamePhase.NAME_SELECTION
    ]:

        logger.info("Dialogue progression -> A")
        manager.controls.press_a()
        time.sleep(0.5)
        return

    time.sleep(0.5)