from smolagents import tool
import logging

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


# =========================
# BASIC ACTION TOOLS
# =========================

@tool
def get_game_state() -> str:
    """
    Returns a string representation of the current emulator game state.

    Use this to:
    - Understand current position, menus, or dialogue
    - Debug unexpected behavior
    - Decide next action

    Returns:
        str: Serialized game state or error message if emulator is missing.
    """
    if not manager:
        return "Error: no emulator"
    return str(_state())


@tool
def move_up() -> str:
    """
    Moves the player character one tile upward in the overworld.

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


# =========================
# PHASE DETECTION
# =========================

from agent.state_detector import StateDetector


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
def navigate_to(target: str) -> str:
    """
    High-level navigation tool that attempts to move the player toward a named target.

    This is an abstract planner tool (NOT step-by-step movement).

    Expected targets may include:
    - "pallet_town"
    - "oak_lab"
    - "pokemart"
    - "pokecenter"
    - "route_1"
    - "grass"
    - custom map labels depending on memory system

    Behavior:
    - Uses internal pathfinding / navigation logic if available in manager
    - Falls back to exploratory movement if no route exists

    Use when:
    - The agent has a clear destination goal
    - Manual movement would be inefficient
    - Recovering from exploration or reset

    Args:
        target (str): Named location or objective

    Returns:
        str: Navigation result or status message
    """
    if not manager:
        return "Error: no emulator"

    if hasattr(manager, "navigation") and hasattr(manager.navigation, "go_to"):
        return str(manager.navigation.go_to(target))

    return f"Navigation not available for target: {target}"

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

    if hasattr(manager, "render") or hasattr(manager, "screenshot"):
        if hasattr(manager, "screenshot"):
            return manager.screenshot()

        if hasattr(manager, "render"):
            return manager.render()

    return "Screenshot not available"
@tool
def debug_state() -> str:
    """
    Returns a structured debug snapshot of the emulator state.

    Use this when:
    - The agent is confused about current game state
    - Debugging stuck behavior
    - Inspecting phase + dialogue detection consistency

    Includes:
    - Raw game state
    - Detected phase
    - Dialogue detection result

    Returns:
        str: Dictionary-like string of debug information
    """
    if not manager:
        return "no manager"

    return str({
        "state": _state(),
        "phase": _detector().detect_phase().name,
        "dialogue": _detector().detect_dialogue(_state())
    })