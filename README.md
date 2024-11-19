# 🧭 Dijkstra's Algorithm Maze Solver

## 🌟 Overview  
This project demonstrates how to solve a maze using **Dijkstra's Algorithm**, which finds the shortest path from a starting point to a goal while avoiding obstacles. The solution is visualized using Matplotlib.  

---

## ✨ Features  
- 🚀 Shortest path calculation using **Dijkstra's Algorithm**.  
- 🔎 Handles obstacles within the maze.  
- 🎨 Visualizes the maze and the resulting path.  

---

## 🛠️ How It Works  

1. The maze is represented as a 2D grid:
   - `0` = Open path 🟩  
   - `1` = Obstacle ⬛  
   - `2` = Shortest path (highlighted after solving) 🟦  

2. The algorithm uses a **priority queue** to explore the shortest path:  
   - Evaluates neighbors to find the least-cost path.  
   - Stops once the goal is reached.  

3. The path is reconstructed and visualized using Matplotlib.  

---

## 📋 Requirements  

### 💻 Prerequisites  
- **Python 3.x**  
- Required libraries:  
  - `matplotlib` 🎨  
  - `numpy` ➕  

### 📥 Installation  
Install the required libraries:  
```bash
pip install matplotlib numpy
```  

---

## 🖥️ Usage  

### 1️⃣ Define Your Maze  
Modify the `maze` variable in the script. Use:  
- `0` for open paths 🟩  
- `1` for obstacles ⬛  

Example:  
```python
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
```  

### 2️⃣ Set Start and Goal Points  
Update the `start` and `goal` variables:  
```python
start = (0, 0)  # Starting point  
goal = (4, 4)  # Goal point  
```  

### 3️⃣ Run the Script  
Execute the program:  
```bash
python dijkstra_maze_solver.py
```  

### 4️⃣ View Results  
- ✅ If a path is found, it will be printed and visualized.  
- ❌ If no path exists, you'll see:  
  ```
  No path found.
  ```  

---

## 🌍 Example  

### Input Maze  
```
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
```  

### Output  
- **Path found:**  
  ```
  Path found: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
  ```  

- **Visualized Maze:**  
  The shortest path is marked in blue.  

---

## 🔧 Customization  

- **Maze Dimensions:** Adjust the size of the grid in the `maze` variable.  
- **Edge Weights:** Currently, all edges have weight `1`. Modify the algorithm to add different weights for more complex scenarios.  

---

## 📜 License  
This project is licensed under the **MIT License**. Feel free to fork, modify, and share! 🌟  

---

🎉 **Happy Solving!** 🧩
