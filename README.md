# Pokémon Red Autonomous AI Agent

An autonomous AI agent that plays Pokémon Red using the PyBoy emulator and a local LLM via SmolAgents.

## Architecture

- **PyBoy Emulator**: Runs the game.
- **RAM Extraction**: Python code reads game state directly from emulator memory.
- **Deterministic Skills**: Python scripts for movement, battles, and recovery.
- **SmolAgents**: Orchestrates high-level planning and tool use.
- **LM Studio**: Hosts the local LLM API (OpenAI-compatible).
- **Qwen2.5-3B-Instruct**: The brain of the agent.

## Prerequisites

1.  **Python 3.10+**
2.  **LM Studio**
3.  **Pokémon Red ROM**: Place `pokemon_red.gb` in the project root.

## Setup Instructions

### 1. LM Studio Setup

1.  Download and install [LM Studio](https://lmstudio.ai/).
2.  Search for and download the **Qwen2.5-3B-Instruct** model.
3.  Go to the **Local Server** tab (the icon that looks like a double arrow/server).
4.  Select the Qwen2.5 model.
5.  Ensure the port is set to `1234`.
6.  Click **Start Server**. The API will be available at `http://localhost:1234/v1`.

### 2. Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

Note: This project does NOT require `torch` or `transformers` as it connects to a local API.

### 3. Running the Agent

Ensure LM Studio local server is running, then execute:

```bash
python main.py
```

## How It Works

- The agent reads the game state (coordinates, party status, map ID) from RAM.
- It sends this state, along with recent history and logic notes, to the LLM.
- The LLM decides on a high-level goal (explore, navigate, battle, etc.) and can call tools to interact with the game.
- Python handles the low-level execution and timing to ensure reliability.
- If the agent gets stuck in a loop, it triggers a recovery mode to move to a new area.

## Project Structure

- `main.py`: The main execution loop.
- `agent/`: Contains the `Planner`, `MemoryStore`, and system prompts.
- `tools/`: smolagents-compatible tools for game interaction.
- `skills/`: Deterministic Python logic for navigation and battles.
- `emulator/`: Manages the PyBoy instance and RAM extraction.
- `config.py`: Configuration settings.
