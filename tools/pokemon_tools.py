from smolagents import tool
import logging
import time
from agent.state_detector import StateDetector

logger = logging.getLogger(__name__)

manager = None


def set_manager(m):
    """
    Sets the global emulator manager instance.

    The manager is required for all game interactions. It should expose:
    - memory.get_game_state()
    - controls (movement + button inputs)
    - pyboy.memory (for state detection)

    Args:
        m: Emulator manager instance
    """
    global manager
    manager = m


def _state():
    """
    Internal helper to fetch the current game state from emulator memory.

    Returns:
        Current game state object or None if manager is not set.
    """
    return manager.memory.get_game_state() if manager else None


@tool
def move_up() -> str:
    """
    Moves the player character one tile upward in the overworld.
    Usually prefer navigate_to tool instead of this.
    Use when:
    - Navigating maps
    - Aligning with doors, NPCs, or exits

    Returns:
        str: "up"
    """
    if not manager:
        return "Error: no emulator"
    manager.controls.move("up")
    return "up"


@tool
def move_down() -> str:
    """
    Moves the player character one tile downward.
    Usually prefer navigate_to tool instead of this.

    Returns:
        str: "down"
    """
    if not manager:
        return "Error: no emulator"
    manager.controls.move("down")
    return "down"


@tool
def move_left() -> str:
    """
    Moves the player character one tile to the left.
    Usually prefer navigate_to tool instead of this.

    Returns:
        str: "left"
    """
    if not manager:
        return "Error: no emulator"
    manager.controls.move("left")
    return "left"


@tool
def move_right() -> str:
    """
    Moves the player character one tile to the right.
    Usually prefer navigate_to tool instead of this.

    Returns:
        str: "right"
    """
    if not manager:
        return "Error: no emulator"
    manager.controls.move("right")
    return "right"


@tool
def press_a() -> str:
    """
    Presses the A button.

    Primary use cases:
    - Confirm selections
    - Advance dialogue
    - Interact with objects/NPCs
    - Select menu options

    Returns:
        str: "A"
    """
    if not manager:
        return "Error: no emulator"
    manager.controls.press("a")
    return "A"


@tool
def press_b() -> str:
    """
    Presses the B button.

    Primary use cases:
    - Cancel actions
    - Exit menus
    - Go back in dialogue

    Returns:
        str: "B"
    """
    if not manager:
        return "Error: no emulator"
    manager.controls.press("b")
    return "B"


@tool
def press_start() -> str:
    """
    Presses START.

    Use for:
    - Opening main menu
    - Pausing gameplay
    - Confirming transitions in some scenes

    Returns:
        str: "START"
    """
    if not manager:
        return "Error: no emulator"
    manager.controls.press_start()
    return "START"


@tool
def press_select() -> str:
    """
    Presses SELECT.

    Use for:
    - Secondary menu interactions (rare in Pokémon Red overworld)
    - Special UI toggles if available

    Returns:
        str: "SELECT"
    """
    if not manager:
        return "Error: no emulator"
    manager.controls.press_select()
    return "SELECT"


@tool
def explore_randomly_tool():
    """
    Executes a built-in random exploration behavior.

    Use when:
    - The agent is stuck
    - No clear objective is available
    - Searching for triggers, exits, or progression events

    Strategy:
    - Random movement + interactions to discover new states

    Returns:
        str: "explore"
    """
    from skills.navigation import explore_randomly
    explore_randomly(manager)
    return "explore"


def _detector():
    """
    Internal helper that creates a StateDetector bound to the current manager.

    Returns:
        StateDetector instance
    """
    return StateDetector(manager)


@tool
def detect_phase() -> str:
    """
    Detects the current high-level game phase.

    Possible outputs may include:
    - TITLE_SCREEN
    - INTRO
    - OAK_DIALOGUE
    - OVERWORLD
    - BATTLE
    - MENU

    Use this to:
    - Choose correct action strategy
    - Avoid invalid inputs in cutscenes or dialogue

    Returns:
        str: Name of the detected phase, or "UNKNOWN"
    """
    if not manager:
        return "UNKNOWN"
    return _detector().detect_phase().name


@tool
def detect_dialogue() -> bool:
    """
    Detects whether the game is currently showing dialogue text.

    Use this to:
    - Decide whether to press A to advance text
    - Avoid movement during scripted scenes

    Returns:
        bool: True if dialogue is active, False otherwise
    """
    if not manager:
        return False
    mem = manager.pyboy.memory
    return _detector().detect_dialogue(mem)


@tool
def detect_title_screen() -> bool:
    """
    Detects whether the game is on the title screen.

    Use this to:
    - Decide whether to press START to begin the game
    - Reset flow if stuck at boot

    Returns:
        bool: True if on title screen
    """
    if not manager:
        return False
    return _detector().detect_title_screen()


@tool
def detect_intro_scene() -> bool:
    """
    Detects whether the game is in early intro scenes (e.g., Oak introduction).

    Use this to:
    - Advance dialogue with A
    - Avoid movement inputs

    Returns:
        bool: True if in intro-related scenes
    """
    if not manager:
        return False
    phase = _detector().detect_phase().name
    return phase in ["INTRO", "OAK_DIALOGUE"]


@tool
def detect_overworld() -> bool:
    """
    Detects whether the player is currently in the overworld (free movement state).

    Use this to:
    - Enable navigation logic
    - Explore map, interact with NPCs, or enter buildings

    Returns:
        bool: True if in overworld
    """
    if not manager:
        return False
    return _detector().detect_phase().name == "OVERWORLD"
@tool
def navigate_to(x: int, y: int) -> str:
    """
    High-level navigation tool that attempts to move the player toward a specific (x, y) coordinate
    manually using Manhattan distance and obstacle recovery logic.

    Args:
        x (int): The target X-coordinate on the current map.
        y (int): The target Y-coordinate on the current map.

    Returns:
        str: Status message of the navigation result.
    """
    if not manager:
        return "Error: no emulator"

    current_x, current_y = manager.memory.get_player_pos()

    max_attempts = 50 
    attempts = 0
    INPUT_DELAY = 0.15 

    while (current_x != x or current_y != y) and attempts < max_attempts:
        attempts += 1
        dx = x - current_x
        dy = y - current_y
        moved = False

        if abs(dx) >= abs(dy) and dx != 0:
            direction = "right" if dx > 0 else "left"
            manager.controls.move(direction)
            time.sleep(INPUT_DELAY)
            
            px, py = manager.memory.get_player_pos()
            if px != current_x or py != current_y:
                current_x, current_y = px, py
                moved = True
            else:
                if dy != 0:
                    alt_direction = "down" if dy > 0 else "up"
                    manager.controls.move(alt_direction)
                    time.sleep(INPUT_DELAY)
                    current_x, current_y = manager.memory.get_player_pos()
                    moved = (current_x != px or current_y != py)

        elif dy != 0:
            direction = "down" if dy > 0 else "up"
            manager.controls.move(direction)
            time.sleep(INPUT_DELAY)
            
            px, py = manager.memory.get_player_pos()
            if px != current_x or py != current_y:
                current_x, current_y = px, py
                moved = True
            else:
                if dx != 0:
                    alt_direction = "right" if dx > 0 else "left"
                    manager.controls.move(alt_direction)
                    time.sleep(INPUT_DELAY)
                    current_x, current_y = manager.memory.get_player_pos()
                    moved = (current_x != px or current_y != py)

        if not moved:
            return f"Navigation stuck near ({current_x}, {current_y}) due to an obstacle. Could not reach ({x}, {y})."

    if current_x == x and current_y == y:
        return f"Successfully navigated to ({x}, {y})."
    else:
        return f"Navigation timed out. Stopped at ({current_x}, {current_y})."
@tool
def save_state(slot: int = 0) -> str:
    """
    Saves emulator state to a given slot.

    Use when:
    - Before risky actions (battles, cutscenes, unknown navigation)
    - After reaching important milestones
    - Creating recovery checkpoints

    Args:
        slot (int): Save slot index (default: 0)

    Returns:
        str: Confirmation message
    """
    if not manager:
        return "Error: no emulator"

    if hasattr(manager, "save_state"):
        manager.save_state(slot)
        return f"Saved state in slot {slot}"

    return "Save system not available"


@tool
def load_state(slot: int = 0) -> str:
    """
    Loads emulator state from a given slot.

    Use when:
    - Agent is stuck or lost
    - Bad action sequence occurred
    - Recovery from undesirable state

    Args:
        slot (int): Save slot index (default: 0)

    Returns:
        str: Confirmation message
    """
    if not manager:
        return "Error: no emulator"

    if hasattr(manager, "load_state"):
        manager.load_state(slot)
        return f"Loaded state from slot {slot}"

    return "Load system not available"


@tool
def take_screenshot() -> str:
    """
    Captures a screenshot of the current emulator frame.

    Use when:
    - Visual confirmation is needed
    - Debugging state detection errors
    - Understanding UI, dialogue, or map context

    Returns:
        str: Path or identifier of saved screenshot, or error message
    """
    if not manager:
        return "Error: no emulator"

    if hasattr(manager, "capture_screen"):
        path = "logs/latest_frame.png"
        manager.capture_screen(path)
        return f"Screenshot saved to {path}"

    return "Screenshot not available"