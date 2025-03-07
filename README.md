# **Conway's Game of Life - Cellular Automata Simulation**

This project is a Python-based simulation of **Conway's Game of Life** using **cellular automata**. It employs the **NumPy** library for efficient data handling and **Matplotlib** for visualization. The objective is to demonstrate how simple local rules can lead to the emergence of complex patterns and behaviors in a grid-based environment.

---

## 📋 **Table of Contents**
- [About the Project](#about-the-project)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Rules of the Game](#rules-of-the-game)
- [Technologies Used](#technologies-used)
- [References](#-📚-references)

---

## 🧐 **About the Project**

Conway's Game of Life is a cellular automaton devised by mathematician John Conway. It consists of a grid of cells that evolve through generations based on a set of simple rules. Despite its simplicity, the Game of Life can produce surprisingly complex behaviors and patterns, such as oscillators, gliders, and stable structures.

This project aims to:
- Simulate Conway's Game of Life on a 2D grid using Python.
- Visualize the evolution of patterns in real-time using Matplotlib.
- Provide a practical example of how cellular automata can model complex systems with simple rules.

---

## 🛠 **Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GabrielSantanaC/cellular-automata.git
   ```
2. Install the required libraries:
   ```bash
   pip install numpy matplotlib
   ```

## 🚀 How to Run
To execute the simulation, run the following command:
   ```bash
   python game_of_life.py
   ```
This will open a Matplotlib window showing the evolution of the grid over time.

## 🕹 Rules of the Game
The Game of Life is governed by four simple rules:

1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors survives to the next generation.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

These rules are applied simultaneously to all cells in each generation.

## 💻 Technologies Used
- Python 3.8+
- NumPy: For efficient grid and array management.
- Matplotlib: For real-time visualization of the grid evolution.

## 📚 References
- Conway, J. H. (1970). Game of Life.
- Wolfram, S. (2002). A New Kind of Science.
- Concepts of Cellular Automata and Complex Systems.
