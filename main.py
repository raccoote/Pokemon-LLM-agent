import time
import logging
import threading
from pathlib import Path

import config
from emulator.pyboy_manager import EmulatorManager
from agent.planner import Planner
from agent.memory_store import MemoryStore
from agent.phase_manager import PhaseManager
from tools.pokemon_tools import set_manager

LOG_PATH = Path(config.LOG_DIR)
LOG_PATH.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH / "agent.log"),
        logging.StreamHandler(),
    ],
)

# Suppress PyBoy sound buffer overrun spam
logging.getLogger("pyboy.core.sound").setLevel(logging.ERROR)
logger = logging.getLogger("PokemonAgent")

def agent_loop(manager, planner, memory):
    """
    Refactored loop using PhaseManager for state-aware execution.
    """
    logger.info("Agent logic thread started")
    
    phase_manager = PhaseManager(manager, memory)
    
    try:
        while True:
            try:
                phase_manager.run_iteration()
            except Exception as e:
                logger.exception("Iteration failed")
                time.sleep(1)
            
            # Small pause between high-level iterations
            time.sleep(0.1)

    except Exception as e:
        logger.error(f"Agent thread crashed: {e}")


def main():
    logger.info("Starting Pokémon Red Autonomous Agent")

    try:
        manager = EmulatorManager()
    except Exception as e:
        logger.error(f"Emulator init failed: {e}")
        return

    # Initialize subsystems
    set_manager(manager)
    planner = Planner()
    memory = MemoryStore()

    # Start the Agent logic in BACKGROUND
    agent_thread = threading.Thread(
        target=agent_loop, 
        args=(manager, planner, memory),
        daemon=True
    )
    agent_thread.start()

    # The MAIN THREAD must keep ticking the window
    logger.info("Main thread now handling emulator window")
    try:
        while True:
            manager.step(1)
            
            # Control frame rate
            if config.SPEED >= 1:
                time.sleep(0.01) # ~60-100 fps
            else:
                pass # Max speed

    except KeyboardInterrupt:
        logger.info("Stopped by user")
    finally:
        manager.stop()

if __name__ == "__main__":
    main()