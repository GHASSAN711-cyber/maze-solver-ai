from queue import PriorityQueue

from utils.utils import get_neighbors, find_start_goal


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def greedy(maze, gui=None):

    start, goal = find_start_goal(maze)

    frontier = PriorityQueue()
    frontier.put((0, start))

    visited = {start}

    parent = {}

    visited_nodes = 0

    while not frontier.empty():

        _, current = frontier.get()

        visited_nodes += 1

        h = heuristic(current, goal)

        print(f"Visiting: {current} h = {h}")

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

                frontier.put(
                    (
                        heuristic(neighbor, goal),
                        neighbor
                    )
                )

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