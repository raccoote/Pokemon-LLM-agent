import logging
from agent.planner import Planner

logger = logging.getLogger(__name__)

class OverworldAgent:
    def __init__(self):
        self.planner = Planner()
        
    def step(self, manager, memory, state):
        """Perform one high-level planning step in the overworld."""
        logger.info("OverworldAgent planning...")
        
        looping = memory.is_looping()
        logic_note = ""
        if looping:
            logger.warning("Loop detected in overworld")
            logic_note = "You are stuck in a loop. Move to a different area immediately."
            
        history = memory.get_history_summary()
        
        try:
            # Re-fetch state for freshness
            current_state = manager.memory.get_game_state()
            
            action = self.planner.get_next_goal(
                state=current_state,
                phase=state.get("phase", "unknown"),
                history=history,
                logic_note=logic_note
            )
            
            # Action is handled by the main loop in phase_manager or by the agent itself?
            # To keep it clean, let's have the agent return the action and the manager execute it.
            return action
            
        except Exception as e:
            logger.exception("OverworldAgent planning failed")
            return {"goal": "explore", "analysis": f"Planning error: {e}"}
