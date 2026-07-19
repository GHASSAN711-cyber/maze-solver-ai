import tkinter as tk
from tkinter import ttk
import time

from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.greedy import greedy
from algorithms.astar import astar
from algorithms.ucs import ucs

from utils.utils import find_start_goal


CELL_SIZE = 40


class MazeGUI:

    def __init__(self, maze):

        self.maze = maze

        self.rows = len(maze)
        self.cols = len(maze[0])

        self.window = tk.Tk()
        self.window.title("Maze Solver AI")
        self.window.configure(bg="#ECECEC")
        self.window.resizable(False, False)


        # ==========================
        # Title
        # ==========================

        title = tk.Label(
            self.window,
            text="Maze Solver AI",
            font=("Arial", 22, "bold"),
            bg="#ECECEC"
        )

        title.pack(pady=10)


        # ==========================
        # Canvas
        # ==========================

        self.canvas = tk.Canvas(
            self.window,
            width=self.cols * CELL_SIZE,
            height=self.rows * CELL_SIZE,
            bg="white"
        )

        self.canvas.pack()


        # ==========================
        # Buttons
        # ==========================

        self.buttons = tk.Frame(
            self.window,
            bg="#ECECEC"
        )

        self.buttons.pack(pady=10)


        self.bfs_btn = tk.Button(
            self.buttons,
            text="BFS",
            width=10,
            command=self.run_bfs
        )

        self.bfs_btn.grid(row=0, column=0, padx=5)


        self.dfs_btn = tk.Button(
            self.buttons,
            text="DFS",
            width=10,
            command=self.run_dfs
        )

        self.dfs_btn.grid(row=0, column=1, padx=5)


        self.greedy_btn = tk.Button(
            self.buttons,
            text="Greedy",
            width=10,
            command=self.run_greedy
        )

        self.greedy_btn.grid(row=0, column=2, padx=5)


        self.astar_btn = tk.Button(
            self.buttons,
            text="A*",
            width=10,
            command=self.run_astar
        )

        self.astar_btn.grid(row=0, column=3, padx=5)
        self.ucs_btn = tk.Button(
    self.buttons,
    text="UCS",
    width=10,
    command=self.run_ucs
)

        self.ucs_btn.grid(row=0, column=4, padx=5)


        self.compare_btn = tk.Button(
        self.buttons,
        text="Compare",
        width=10,
        command=self.compare_all
        )

        self.compare_btn.grid(row=0, column=5, padx=5)


        self.reset_btn = tk.Button(
            self.buttons,
            text="Reset",
            width=10,
            command=self.reset
        )

        self.reset_btn.grid(row=0, column=6, padx=5)


        # ==========================
        # Information
        # ==========================

        self.info = tk.Label(
            self.window,
            text="Algorithm: -\nVisited: -\nPath: -\nTime: -",
            bg="#ECECEC",
            font=("Arial", 12)
        )

        self.info.pack(pady=10)


        self.draw_maze() 
            # ==========================
    # BFS
    # ==========================

    def run_bfs(self):

        self.reset()

        start = time.perf_counter()

        path, visited = bfs(self.maze, self)

        elapsed = time.perf_counter() - start


        if path:

            self.draw_path(path)

            self.update_info(
                "BFS",
                visited,
                len(path),
                elapsed
            )


    # ==========================
    # DFS
    # ==========================

    def run_dfs(self):

        self.reset()

        start = time.perf_counter()

        path, visited = dfs(self.maze, self)

        elapsed = time.perf_counter() - start


        if path:

            self.draw_path(path)

            self.update_info(
                "DFS",
                visited,
                len(path),
                elapsed
            )


    # ==========================
    # Greedy
    # ==========================

    def run_greedy(self):

        self.reset()

        start = time.perf_counter()

        path, visited = greedy(self.maze, self)

        elapsed = time.perf_counter() - start


        if path:

            self.draw_path(path)

            self.update_info(
                "Greedy",
                visited,
                len(path),
                elapsed
            )


    # ==========================
    # A*
    # ==========================

    def run_astar(self):

        self.reset()

        start = time.perf_counter()

        path, visited = astar(self.maze, self)

        elapsed = time.perf_counter() - start


        if path:

            self.draw_path(path)

            self.update_info(
                "A*",
                visited,
                len(path),
                elapsed
            )
    # ==========================
# Uniform Cost Search
# ==========================

    def run_ucs(self):

     self.reset()

     start = time.perf_counter()

     path, visited = ucs(self.maze, self)

     elapsed = time.perf_counter() - start

     if path:

         self.draw_path(path)

         self.update_info(
            "Uniform Cost Search",
            visited,
            len(path),
            elapsed
        )


    # ==========================
    # Compare
    # ==========================

    def compare_all(self):

     algorithms = [
        ("BFS", bfs),
        ("DFS", dfs),
        ("Greedy", greedy),
        ("A*", astar),
        ("UCS", ucs)
    ]

     results = []

     for name, algorithm in algorithms:

        start = time.perf_counter()

        path, visited = algorithm(self.maze)

        elapsed = time.perf_counter() - start

        results.append((
            name,
            visited,
            len(path) if path else 0,
            round(elapsed, 6)
        ))

     self.show_comparison(results)

    def show_comparison(self, results):

     window = tk.Toplevel(self.window)
     window.title("Algorithm Comparison")

     tree = ttk.Treeview(
         window,
        columns=("Algorithm", "Visited", "Path", "Time"),
        show="headings",
        height=5
    )

     tree.heading("Algorithm", text="Algorithm")
     tree.heading("Visited", text="Visited")
     tree.heading("Path", text="Path")
     tree.heading("Time", text="Time (sec)")

     tree.column("Algorithm", width=120, anchor="center")
     tree.column("Visited", width=80, anchor="center")
     tree.column("Path", width=80, anchor="center")
     tree.column("Time", width=100, anchor="center")

     for row in results:
        tree.insert("", tk.END, values=row)

     tree.pack(padx=10, pady=10)


    # ==========================
    # Draw Maze
    # ==========================

    def draw_maze(self):

        self.canvas.delete("all")


        for r in range(self.rows):

            for c in range(self.cols):

                x1 = c * CELL_SIZE
                y1 = r * CELL_SIZE

                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE


                cell = self.maze[r][c]


                if cell == "#":
                    color = "black"

                elif cell == "A":
                    color = "green"

                elif cell == "B":
                    color = "red"

                else:
                    color = "white"


                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color,
                    outline="gray"
                )


    # ==========================
    # Draw Path
    # ==========================

    def draw_path(self, path):

        for r, c in path:

            x1 = c * CELL_SIZE
            y1 = r * CELL_SIZE

            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE


            self.canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill="cyan",
                outline="gray"
            )

            self.window.update()

            time.sleep(0.05)


    # ==========================
    # Visit Animation
    # ==========================

    def visit_cell(self, r, c):

        x1 = c * CELL_SIZE
        y1 = r * CELL_SIZE

        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE


        self.canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            fill="yellow",
            outline="gray"
        )


        self.window.update()

        time.sleep(0.02)


    # ==========================
    # Update Info
    # ==========================

    def update_info(
            self,
            algorithm,
            visited,
            path,
            elapsed):

        self.info.config(
            text=
            f"Algorithm: {algorithm}\n"
            f"Visited: {visited}\n"
            f"Path: {path}\n"
            f"Time: {round(elapsed,6)} sec"
        )


    # ==========================
    # Reset
    # ==========================

    def reset(self):

        self.draw_maze()


    # ==========================
    # Start GUI
    # ==========================
    def show(self):

         self.window.mainloop()

    def run(self):

        self.window.mainloop()