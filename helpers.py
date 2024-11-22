from typing import List
from random import random
from math import floor
from constants import ROWS, COLS, BOXES

def convertUserInput(input: str) -> int:
    # convert user input from form of 'A3', 'I9', etc. into grid index

    if len(input) != 2:
        raise Exception("Input has incorrect length")

    colStr = input[0]
    rowStr = input[1]
    if not colStr.isupper() or not rowStr.isdigit():
        raise Exception("Input in incorrect form")
    
    colInt = ord(colStr)
    rowInt = int(rowStr)
    if rowInt < 1 or rowInt > 9 or colInt < 65 or colInt > 73:
        raise Exception("Input value(s) out of bounds")
    
    index = (9 * (rowInt - 1)) + (colInt - 65)
    if index > 80:
        raise Exception("Resulting value is too large")
    return index

def checkRow(grid: List[int], idx: int, digit: int):
    # determine whether digit can be placed into row

    # find row associated with index value (ie. 0-8)
    rowIdx = [i for i in range(len(ROWS)) if idx in ROWS[i]][0]
    # print(f"{idx} is in row {rowIdx + 1}")

    rowCross = ROWS[rowIdx]                     # indices to check in grid
    gridRow = [grid[r] for r in rowCross]       # actual row values
    return digit not in gridRow

def checkCol(grid: List[int], idx: int, digit: int):
    # determine whether digit can be placed into col

    # find col associated with index value (ie. A-I represented as 0-8)
    colIdx = [i for i in range(len(COLS)) if idx in COLS[i]][0]
    # print(f"{idx} is in col {colIdx + 1}")

    colCross = COLS[colIdx]                     # indices to check in grid
    gridCol = [grid[c] for c in colCross]       # actual column values
    return digit not in gridCol

def checkBox(grid: List[int], idx: int, digit: int):
    # determine whether digit can be placed into box

    # find box associated with index value (ie. 0-8)
    boxIdx = [i for i in range(len(BOXES)) if idx in BOXES[i]][0]
    # print(f"{idx} is in box {boxIdx + 1}")

    boxCross = BOXES[boxIdx]                    # indices to check in grid
    gridBox = [grid[b] for b in boxCross]       # actual box values
    return digit not in gridBox

def generateDigit():
    # generate random number between 1-9 (inclusive)
    return floor(random() * 9 + 1)

def generateIndex():
    # generate random grid index between 0-80 (inclusive)
    return floor(random() * 81)