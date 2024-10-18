from typing import List
from constants import ROWS, COLS, BOXES

class Grid:
    grid: List[int] = None

    def __init__(self):
        self.grid = [0 for _ in range(81)]
    
    def __str__(self):
        ret = "\n      A   B   C    D   E   F    G   H   I"
        printGrid = [str(v) if v > 0 else " " for v in self.grid]
        for i,v in enumerate(printGrid):
            if i % 27 == 0:
                ret += "\n   " + "-"*41
            if i % 9 == 0:
                ret += f"\n{int((i/9) + 1)}  ||"
            ret += f" {v} |"
            if i % 3 == 2:
                ret += "|"

        ret += "\n   " + "-"*41 + "\n"
        return ret
    
    def placeDigit(self, idx: int, digit: int):
        # places digit in index, regardless of current contents there
        self.grid[idx] = digit
