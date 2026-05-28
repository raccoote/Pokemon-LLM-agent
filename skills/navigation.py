import logging
import random

logger = logging.getLogger(__name__)

def navigate_to(manager, target_x, target_y):
    """
    Primitive navigation skill.
    TODO: Integrate proper A* pathfinding.
    """
    curr_x, curr_y = manager.memory.get_player_pos()
    
    # Simple Manhattan movement
    if curr_x < target_x:
        manager.controls.move("right")
    elif curr_x > target_x:
        manager.controls.move("left")
    elif curr_y < target_y:
        manager.controls.move("down")
    elif curr_y > target_y:
        manager.controls.move("up")
    
    return True

def explore_randomly(manager):
    """Random movement to find something interesting."""
    directions = ["up", "down", "left", "right"]
    dir = random.choice(directions)
    manager.controls.move(dir)
    return True
