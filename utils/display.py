def print_maze(maze, path=None):

    maze_copy = []

    for row in maze:
        maze_copy.append(list(row))


    if path:

        for position in path:

            r, c = position

            if maze_copy[r][c] not in ["A", "B"]:

                maze_copy[r][c] = "*"



    print("\n=== Maze ===\n")


    for row in maze_copy:

        print(
            "".join(row)
        )


    print()