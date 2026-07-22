from gui.window import MazeGUI
from data.maze import maze



def main():

    app = MazeGUI(maze)

    app.show()


if __name__ == "__main__":

    main()