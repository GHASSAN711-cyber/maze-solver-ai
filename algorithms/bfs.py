from collections import deque

from utils.utils import get_neighbors, find_start_goal


def bfs(maze, gui=None):

    start, goal = find_start_goal(maze)

    queue = deque([start])

    visited = {start}

    parent = {}

    visited_nodes = 0

    while queue:

        current = queue.popleft()

        visited_nodes += 1

        print("Visiting:", current)

        if gui:
            gui.visit_cell(current[0], current[1])

        if current == goal:

            print("Goal Found!")

            path = reconstruct_path(parent, start, goal)

            return path, visited_nodes

        for neighbor in get_neighbors(maze, current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    print("No Path Found")

    return None, visited_nodes


def reconstruct_path(parent, start, goal):

    path = []

    current = goal

    while current != start:

        path.append(current)

        current = parent[current]

    path.append(start)

    path.reverse()

    return path