# أدوات مشتركة للمشروع


# إيجاد البداية والهدف
def find_start_goal(maze):

    start = None
    goal = None

    for row in range(len(maze)):
        for col in range(len(maze[row])):

            if maze[row][col] == "A":
                start = (row, col)

            elif maze[row][col] == "B":
                goal = (row, col)

    return start, goal



# إيجاد الجيران
def get_neighbors(maze, position):

    directions = [
        (-1, 0),  # أعلى
        (1, 0),   # أسفل
        (0, -1),  # يسار
        (0, 1)    # يمين
    ]

    neighbors = []

    row, col = position

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        # التأكد أننا داخل حدود المتاهة
        if (
            new_row >= 0 and
            new_row < len(maze) and
            new_col >= 0 and
            new_col < len(maze[0])
        ):

            # التأكد أنها ليست جدارًا
            if maze[new_row][new_col] != "#":

                neighbors.append((new_row, new_col))

    return neighbors



# Heuristic - Manhattan Distance
def heuristic(current, goal):

    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])