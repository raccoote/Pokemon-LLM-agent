import logging

logger = logging.getLogger(__name__)

def close_all_menus(manager):
    """Spams B to escape any open menus."""
    for _ in range(5):
        manager.controls.press("b", ticks=10)
        manager.controls.wait(5)

def save_game_in_menu(manager):
    """Scripted menu navigation to save the game."""
    # Press Start
    manager.controls.press("start", ticks=15)
    manager.controls.wait(20)
    # Move to SAVE (usually 4-5 items down depending on state)
    for _ in range(4):
        manager.controls.press("down", ticks=10)
        manager.controls.wait(10)
    # Press A
    manager.controls.press("a", ticks=10)
    manager.controls.wait(30)
    # Confirm Save with A
    manager.controls.press("a", ticks=10)
    manager.controls.wait(100) # Wait for save
    # Close Menu
    manager.controls.press("b", ticks=10)
