from utils.utils import get_neighbors, find_start_goal


def dfs(maze, gui=None):

    start, goal = find_start_goal(maze)

    visited = set()

    parent = {}

    visited_nodes = 0


    def search(current):

        nonlocal visited_nodes

        visited.add(current)

        visited_nodes += 1

        print("Visiting:", current)

        if gui:
            gui.visit_cell(current[0], current[1])


        if current == goal:

            print("Goal Found!")

            return True


        for neighbor in get_neighbors(maze, current):

            if neighbor not in visited:

                parent[neighbor] = current

                if search(neighbor):

                    return True


        return False


    found = search(start)


    if found:

        path = reconstruct_path(parent, start, goal)

        return path, visited_nodes


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