from gui.window import MazeGUI

maze = [
    "#############",
    "#A    #    B#",
    "# ### # ### #",
    "#     #     #",
    "### ### ### #",
    "#           #",
    "#############"
]

app = MazeGUI(maze)
app.show()