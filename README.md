# AI-Lab1-RoshanShrestha-021368

# Vacuum Cleaner Agents 🧹

This repository contains implementations of three types of intelligent agents for a vacuum cleaner environment in a 10x10 grid. The agents demonstrate different AI strategies: Simple Reflex, Goal-Based, and Utility-Based. The purpose is to simulate how each agent interacts with the environment to clean dirty cells efficiently.

---

## Environment Setup

- **Grid Size:** 10x10 (100 cells)
- **Cell States:** Each cell can be either `clean` or `dirty`.
- **Actions Available:** `Move Up`, `Move Down`, `Move Left`, `Move Right`, `Suck`
- **Initial Position:** Agent starts at a random position in the grid.
- **Goal:** Clean all dirty cells efficiently.

---

## 1. Simple Reflex Agent

### 🔍 Description:
A simple reflex agent selects actions based solely on the **current percept**—i.e., whether the current cell is dirty or clean.

### 🔧 Behavior:
- If the current cell is dirty, it performs the `suck` action.
- If the current cell is clean, it moves randomly to one of the adjacent cells.

### 🧪 Simulation:
- The agent runs for **20 steps**.
- The **grid state is displayed after each step** to visualize the cleaning process.

---

## 2. Goal-Based Agent

### 🔍 Description:
This agent maintains an **internal model** of the environment to track which cells are dirty. It uses this model to make decisions that help it achieve the goal of a clean grid.

### 🔧 Behavior:
- Continuously updates its internal map of clean and dirty cells.
- Uses a **simple search strategy** (e.g., nearest dirty cell) to decide the next move.
- Moves toward dirty cells and cleans them.

### 🧪 Simulation:
- The agent continues **until the entire grid is clean**.
- Displays the **sequence of actions taken** and the **final grid state**.

---

## 3. Utility-Based Agent

### 🔍 Description:
A utility-based agent chooses actions based on a **utility function** that rewards cleanliness and penalizes unnecessary movement.

### ⚙️ Utility Function:
- `+5` for cleaning a dirty cell
- `-1` for each movement step

### 🔧 Behavior:
- Evaluates all possible actions.
- Selects the action that **maximizes the expected utility** at each step.
- Keeps track of cumulative utility.

### 🧪 Simulation:
- Displays the **sequence of actions taken**.
- Shows the **final grid state**.
- Outputs the **total utility score** achieved.

---

## 🎯 Objective

This project demonstrates how different types of intelligent agents behave in the same environment using different decision-making strategies. It helps understand key AI concepts such as reflex actions, goal formulation, and utility optimization.

---

## 📌 Requirements

- Python 3.x
- No external libraries required
