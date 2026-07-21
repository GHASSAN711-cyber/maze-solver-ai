from collections import deque
from utils.utils import find_start_goal, get_neighbors


def reconstruct_path(meeting, forward_parent, backward_parent):
    # المسار من البداية إلى نقطة الالتقاء
    path_forward = []
    node = meeting

    while node is not None:
        path_forward.append(node)
        node = forward_parent[node]

    path_forward.reverse()

    # المسار من نقطة الالتقاء إلى الهدف
    path_backward = []
    node = backward_parent[meeting]

    while node is not None:
        path_backward.append(node)
        node = backward_parent[node]

    return path_forward + path_backward


def Bidirectional(maze, gui=None):

    start, goal = find_start_goal(maze)

    if start == goal:
        return [start], 1

    forward_queue = deque([start])
    backward_queue = deque([goal])

    forward_visited = {start}
    backward_visited = {goal}

    forward_parent = {start: None}
    backward_parent = {goal: None}

    visited_count = 0

    while forward_queue and backward_queue:

        # ==========================
        # Forward Search
        # ==========================

        current = forward_queue.popleft()
        visited_count += 1

        if gui:
            gui.visit_cell(*current)

        for neighbor in get_neighbors(maze, current):

            if neighbor not in forward_visited:

                forward_visited.add(neighbor)
                forward_parent[neighbor] = current
                forward_queue.append(neighbor)

                if neighbor in backward_visited:

                    path = reconstruct_path(
                        neighbor,
                        forward_parent,
                        backward_parent
                    )

                    return path, visited_count

        # ==========================
        # Backward Search
        # ==========================

        current = backward_queue.popleft()
        visited_count += 1

        if gui:
            gui.visit_cell(*current)

        for neighbor in get_neighbors(maze, current):

            if neighbor not in backward_visited:

                backward_visited.add(neighbor)
                backward_parent[neighbor] = current
                backward_queue.append(neighbor)

                if neighbor in forward_visited:

                    path = reconstruct_path(
                        neighbor,
                        forward_parent,
                        backward_parent
                    )

                    return path, visited_count

    return None, visited_count