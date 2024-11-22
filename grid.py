from typing import List

from helpers import checkBox, checkCol, checkRow
from helpers import generateDigit, generateIndex
from constants import BOXES

class Grid:
    grid: List[int] = None
    missing_digits: int = -1

    def __init__(self, md: int = 1):
        self.grid = [0 for _ in range(81)]
        self.missing_digits = md
        self.prepareGrid()
    
    def __str__(self):
        ret = "\n      A   B   C    D   E   F    G   H   I"
        printGrid = [str(v) if v > 0 else " " for v in self.grid]
        for i,v in enumerate(printGrid):
            if i % 27 == 0:             # vertical separation between boxes
                ret += "\n   " + "-"*41
            if i % 9 == 0:              # standard new line, row number
                ret += f"\n{int((i/9) + 1)}  ||"
            ret += f" {v} |"
            if i % 3 == 2:              # horizontal separation between boxes
                ret += "|"

        ret += "\n   " + "-"*41 + "\n"
        return ret
    
    def placeDigit(self, idx: int, digit: int):
        # places digit in index, regardless of current contents there
        self.grid[idx] = digit
    
    def isValidMove(self, idx: int, digit: int):
        # checks whether placing `digit` into `idx` is allowed
        return checkRow(self.grid, idx, digit) and checkCol(self.grid, idx, digit) and checkBox(self.grid, idx, digit)
    
    def isComplete(self):
        # finished when all 0s gone
        return not 0 in self.grid
    
    # ------------ FUNCTIONS FOR FILLING IN GRID ------------
    # inspired by https://www.geeksforgeeks.org/program-sudoku-generator/
    def prepareGrid(self):
        # fill boxes along diagonal
        self.fillDiagonal()

        # fill any remaining blocks
        self.fillRemaining(3)

        # remove `missing_digits` digits
        self.removeDigits()
    
    def fillDiagonal(self):
        # TODO: maybe make this a little better lol
        self.fillBox(0)
        self.fillBox(4)
        self.fillBox(8)

    def fillBox(self, boxIdx: int):
        boxIdcs = BOXES[boxIdx]
        for i in boxIdcs:
            while True:         # repeatedly generate digits until a valid one found
                num = generateDigit()
                if checkBox(self.grid, i, num):
                    break
            self.placeDigit(i, num)

    def fillRemaining(self, startIdx: int):
        if startIdx >= 80:      # check if at end of grid
            return True
        if self.grid[startIdx] != 0:        # skip non-empty values
            return self.fillRemaining(startIdx + 1)
        
        # try filling in current cell with valid value
        for num in range(1, 10):
            if self.isValidMove(startIdx, num):
                self.placeDigit(startIdx, num)
                if self.fillRemaining(startIdx + 1):        # continue to next index
                    return True
                self.placeDigit(startIdx, 0)
        
        # no valid value found, start backtracking
        return False

    def removeDigits(self):
        count = self.missing_digits
        
        while count != 0:
            randIdx = generateIndex()       # pick a random index
            if self.grid[randIdx] != 0:     # if occupied, empty space
                self.placeDigit(randIdx, 0)
                count -= 1