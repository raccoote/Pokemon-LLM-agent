from enum import Enum, auto

class GamePhase(Enum):
    BOOT = auto()           # Nintendo screen / Blank
    TITLE = auto()          # Title screen ("Press START")
    MENU = auto()           # Main menu (New Game/Continue)
    INTRO = auto()          # Gengar/Nidorino cutscene
    DIALOGUE = auto()   # Oak introduction
    NAME_SELECTION = auto() # Player/Rival naming
    BEDROOM = auto()        # Initial spawn in Pallet Town
    OVERWORLD = auto()      # Normal gameplay
    BATTLE = auto()         # In-battle
    UNKNOWN = auto()

