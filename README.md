Pokémon Red: Agent LLM

This project is a Pokémon Red agent built with Python, PyBoy, SmolAgents, and a locally hosted LLM using Qwen2.5-3B-Instruct.

The architecture is inspired by MCP agents, where the language model interacts with pre-defined tools instead of directly controlling the environment. Rather than sending raw button presses frame-by-frame, the model operates as a high-level planner that selects goals and actions (e.g. open inventory).

The model observes the current game state, selects objectives, and calls structured tools that will execute deterministic actions inside the emulator.

<img width="1074" height="911" alt="image" src="https://github.com/user-attachments/assets/e78c487f-ee2e-449f-a6ea-56f84cca875b" />

---

<img width="1074" height="672" alt="image" src="https://github.com/user-attachments/assets/6c8ab02d-c34c-496f-aa68-c7956f68ce6f" />

---

# Workflow

```text
PyBoy Emulator 
    ↓
RAM extraction 
    ↓
Structured game state
    ↓
SmolAgents + Qwen2.5-3b
    ↓
Tool calls
    ↓
Python execution layer
    ↓
PyBoy button inputs
```

The game (Pokemon Red) runs through the PyBoy Game Boy emulator (https://github.com/baekalfen/pyboy).

Python reads important values (such as pokemon hp, states, coordinates) directly from emulator memory (using this fan-made ram map -> https://datacrystal.tcrf.net/wiki/Pok%C3%A9mon_Red_and_Blue/RAM_map). That data gets passed into the LLM through SmolAgents library by Hugging Face.

The model then decides what to do next using any of the tools available:

* heal pokemon
* retrieve Gamestate (battle, dialogue, cutscene)
* navigate somewhere
* interact with menus

The actual execution is handled directly by Python code. 

For example:
```
def navigate_to(manager, target_x, target_y):
    """
    Navigation skill using Manhattan movement.
    """
    curr_x, curr_y = manager.memory.get_player_pos()
    
    if curr_x < target_x:
        manager.controls.move("right")
    elif curr_x > target_x:
        manager.controls.move("left")
    elif curr_y < target_y:
        manager.controls.move("down")
    elif curr_y > target_y:
        manager.controls.move("up")
    
    return True
```

---

# Setup Guide

## 1. Install Python dependencies

Inside the project folder:

```bash
pip install -r requirements.txt
```

## 2. Install LM Studio 

(I used LM Studio, but you can set up your LLM model in different ways.)

Download and install LM Studio:

https://lmstudio.ai/

Inside LM Studio, :


1. Download the model you want:
```text
Qwen2.5-3B-Instruct
```
2. Open the “Developer” tab
3. Load the model
4. Start the local server

The API runs by default at the URL:

```text
http://localhost:1234/v1
```

## 3. Add the ROM

Place your Pokémon Red ROM in the project root:

```text
pokemon_red.gb
```

## 4. Run the agent

```bash
python main.py
```
