from queue import PriorityQueue

from utils.utils import get_neighbors, find_start_goal


def ucs(maze, gui=None):

    start, goal = find_start_goal(maze)

    frontier = PriorityQueue()
    frontier.put((0, start))

    parent = {}

    cost_so_far = {
        start: 0
    }

    visited_nodes = 0

    while not frontier.empty():

        current_cost, current = frontier.get()

        visited_nodes += 1

        print(
            f"Visiting: {current} | Cost = {current_cost}"
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

            new_cost = current_cost + 1

            if (
                neighbor not in cost_so_far
                or
                new_cost < cost_so_far[neighbor]
            ):

                cost_so_far[neighbor] = new_cost

                parent[neighbor] = current

                frontier.put(
                    (
                        new_cost,
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