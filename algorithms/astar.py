from queue import PriorityQueue

from utils.utils import get_neighbors, find_start_goal


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(maze, gui=None):

    start, goal = find_start_goal(maze)

    frontier = PriorityQueue()
    frontier.put((0, start))

    parent = {}

    g_score = {
        start: 0
    }

    visited = set()

    visited_nodes = 0

    while not frontier.empty():

        _, current = frontier.get()

        if current in visited:
            continue

        visited.add(current)

        visited_nodes += 1

        g = g_score[current]
        h = heuristic(current, goal)
        f = g + h

        print(
            f"Visiting: {current} | g = {g} | h = {h} | f = {f}"
        )

        if gui:
            gui.visit_cell(current[0], current[1])

        if current == goal:

            print("Goal Found!")

            path = reconstruct_path(
                parent,
                start,
                goal
            )

            return path, visited_nodes

        for neighbor in get_neighbors(maze, current):

            new_g = g + 1

            if neighbor not in g_score or new_g < g_score[neighbor]:

                g_score[neighbor] = new_g

                parent[neighbor] = current

                new_f = new_g + heuristic(neighbor, goal)

                frontier.put(
                    (
                        new_f,
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