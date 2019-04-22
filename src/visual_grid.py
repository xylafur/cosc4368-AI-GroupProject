# Imports for support of reading posiitons
import re
from pathlib import Path
from tkinter import *


# NOTES:
# (\d+\t\t\t+(\(\d\S\s\d\)\t\t\t\w+))
# Returns:0			(1, 1)			False
# From:/src/ExperimentOutput/Experiment1_1.txt
class Cell():
    FILLED_COLOR_BG = "red"
    EMPTY_COLOR_BG = "white"
    FILLED_COLOR_BORDER = "green"
    EMPTY_COLOR_BORDER = "black"

    # def get_movement_data(self,path, regex_list,match_num_list,x_list,y_list,block_list):
    #
    #     path_ = path
    #     regex_ = regex_list
    #     match_num_list_ = match_num_list
    #     x_list_ = x_list
    #     y_list_ = y_list
    #     block_list_ = block_list
    #
    #
    #     return match_num_list, x_list, y_list, block_list

    def __init__(self, master, x, y, size):
        """ Constructor of the object called by Cell(...) """
        self.master = master
        self.abs = x
        self.ord = y
        self.size = size
        self.fill = False

    def _switch(self):
        """ Switch if the cell is filled or not. """
        self.fill = not self.fill

    def draw(self):

        if self.master != None:
            fill = Cell.FILLED_COLOR_BG
            outline = Cell.FILLED_COLOR_BORDER

            if not self.fill:
                fill = Cell.EMPTY_COLOR_BG
                outline = Cell.EMPTY_COLOR_BORDER

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill=fill, outline=outline)


class CellGrid(Canvas):
    def __init__(self, master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width=cellSize * columnNumber, height=cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize

        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize))

            self.grid.append(line)
        x = []
        y = []
        self.get_movement_data(x, y)

        # memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []
        for row in x:
            for col in y:
                cell = self.grid[row][col]
                cell._switch()
                cell.draw()
                # add the cell to the list of cell switched during the click
                self.switched.append(cell)
        # bind click action
        self.bind("<Button-1>", self.handleMouseClick)
        # bind moving while clicking
        self.bind("<B1-Motion>", self.handleMouseMotion)
        # bind release button action - clear the memory of midified cells.
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        self.draw()

    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def get_movement_data(self, x_list, y_list):

        # path_ = path
        x_list_ = x_list
        y_list_ = y_list
        txt = Path(
            '/Users/henryrodriguez/PycharmProjects/cosc4368-AI-GroupProject/src/ExperimentOutput/Experiment1_1.txt').read_text()

        regex_x = r"\t+\((\d)"
        regex_y = r"\t+\(\d\S\s(\d)"
        matches_x = re.finditer(regex_x, txt, re.MULTILINE)
        move_x = []
        for matchNum, match in enumerate(matches_x, start=1):
            # print("{match}".format(match=match.group()))
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                move_x.append(match.group(groupNum))
        # print(move_x)

        matches_y = re.finditer(regex_y, txt, re.MULTILINE)
        move_y = []
        for matchNum, match in enumerate(matches_y, start=1):
            # print("{match}".format(match=match.group()))
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                move_y.append(match.group(groupNum))
        # print(move_y)
        x_list = move_x
        y_list = move_y
        print(x_list)
        return x_list, y_list

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        cell._switch()
        cell.draw()
        # add the cell to the list of cell switched during the click
        self.switched.append(cell)

    def handleMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell._switch()
            cell.draw()
            self.switched.append(cell)


if __name__ == "__main__":
    app = Tk()

    grid = CellGrid(app, 5, 5, 20)
    grid.pack()

    app.mainloop()
