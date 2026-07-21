## 🧩 AI Maze Solver

مشروع ذكاء اصطناعي لحل المتاهات باستخدام خوارزميات البحث.



# 📌 Overview

Maze Solver AI is a desktop application developed using **Python** and **Tkinter** to demonstrate, visualize, and compare classical Artificial Intelligence search algorithms.

The project allows users to watch how each algorithm explores a maze in real time, compare their performance, and understand the strengths and weaknesses of different search techniques.

This project was created as part of my Artificial Intelligence learning journey while studying Electrical Engineering.

---

# 🚀 Features

✅ Interactive graphical interface

✅ Real-time search visualization

✅ Animated visited nodes

✅ Animated shortest path

✅ Algorithm performance comparison

✅ Execution time measurement

✅ Number of visited nodes

✅ Path length calculation

✅ Clean and organized project structure

---

# 🤖 Implemented Algorithms

| Algorithm | Status |
|------------|--------|
| Breadth First Search (BFS) | ✅ |
| Depth First Search (DFS) | ✅ |
| Greedy Best First Search | ✅ |
| A* Search | ✅ |
| Uniform Cost Search (UCS) | ✅ |
| Bidirectional Search | ✅ |

---

# 📊 Performance Comparison

The application compares all implemented algorithms based on:

- Number of visited nodes
- Path length
- Execution time
- Search behavior
- Visualization

---

# 🛠 Technologies Used

- Python
- Tkinter
- Git
- GitHub
- Markdown

---

# 📂 Project Structure

```text
maze_solver_ai/
│
├── algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   ├── greedy.py
│   ├── astar.py
│   ├── ucs.py
│   └── Bidirectional.py
│
├── data/
│   └── maze.py
│
├── gui/
│   └── window.py
│
├── utils/
│   └── utils.py
│
├── README.md
├── main.py
└── .gitignore
```

---

# ▶️ How To Run

1. Clone the repository

```bash
https://github.com/GHASSAN711-cyber/maze-solver-ai.git
```

2. Open the project

```bash
cd maze_solver_ai
```

3. Run the application

```bash
python main.py
```

---

# 📷 Screenshots

## Main Interface

*Screenshot will be added soon.*

---

## Algorithm Comparison

*Screenshot will be added soon.*

---

# 🎯 Project Objectives

This project aims to:

- Understand classical AI search algorithms.
- Compare different search strategies.
- Improve algorithm visualization.
- Build a professional AI portfolio.
- Practice clean software architecture.

---

# 📈 Learning Outcomes

Through this project I learned:

- Artificial Intelligence Search Algorithms
- Python Programming
- GUI Development using Tkinter
- Project Organization
- Git & GitHub Workflow
- Technical Documentation using Markdown
- Debugging and Problem Solving

---

# 🔮 Future Improvements

- Dijkstra Algorithm
- IDDFS
- Beam Search
- Random Maze Generator
- Adjustable Animation Speed
- Dark Theme
- Export Statistics
- Save Maze Results
- Weighted Mazes
- Custom Maze Editor

---

# 👨‍💻 Developer

**Ghassan Al-Dhuraibi**

Electrical Engineering Student

AI Developer

Python Programmer

---

# 🌐 Professional Profiles

GitHub:

> *https://github.com/GHASSAN711-cyber

Fiverr:

> **Karavolt**

Upwork:

> https://www.upwork.com/freelancers

---

## 📸 Screenshots

### Main Interface

![Main Interface](./screenshots/main_interface.png)

### A* Algorithm Solution

![A* Solution](./screenshots/astar_solution.png)

### BFS Algorithm Solution

![BFS Solution](./screenshots/bfs_solution.png)

### DFS Algorithm Solution

![DFS Solution](./screenshots/dfs_solution.png)

---

# 📄 License

This project was created for educational and portfolio purposes.

Feel free to explore, learn, and improve the project.

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

It helps support my learning journey and motivates me to build more AI projects.

---

# 🚀 Karavolt

**Where AI Meets Engineering. ⚡🤖**

# 📊 Algorithm Performance Analysis

## BFS (Breadth First Search)

### Time Complexity
O(V + E)

حيث:
- V عدد الخلايا أو العقد في المتاهة.
- E عدد الاتصالات بين الخلايا.

### Space Complexity
O(V)

لأن الخوارزمية تخزن جميع العقد التي تمت زيارتها.

---

## DFS (Depth First Search)

### Time Complexity
O(V + E)

### Space Complexity
O(V)

بسبب تخزين مسار البحث والعقد المكتشفة.

---

## A* Algorithm

### Time Complexity
O(E)

تعتمد على جودة Heuristic المستخدمة.

### Space Complexity
O(V)

لأنها تحتفظ بقائمة Open و Closed.

---

## Greedy Best First Search

### Time Complexity
O(V)

### Space Complexity
O(V)

---

## Uniform Cost Search (UCS)

### Time Complexity
O(E log V)

باستخدام Priority Queue.

### Space Complexity
O(V)

# 🚀 How to Run

## Requirements

Make sure you have Python installed.

Install the required libraries:

```bash
pip install -r requirements.txt
Run the Application

Navigate to the project folder:

cd maze_solver_ai

Run:

python main.py

The application will open the Maze Solver graphical interface.

🖥️ Project Interface

The project provides a graphical interface that allows users to visualize maze solving algorithms and compare their performance.

Supported algorithms:

Breadth First Search (BFS)
Depth First Search (DFS)
A* Search
Greedy Best First Search
Uniform Cost Search (UCS)
Bidirectional Search
