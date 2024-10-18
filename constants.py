# indices associated with each row
ROWS = [
    list(range(0, 9)),
    list(range(9, 18)),
    list(range(18, 27)),
    list(range(27, 36)),
    list(range(36, 45)),
    list(range(45, 54)),
    list(range(54, 63)),
    list(range(63, 72)),
    list(range(72, 81))
]

# indices associated with each column
COLS = [
    list(range(0, 81, 9)),
    list(range(1, 81, 9)),
    list(range(2, 81, 9)),
    list(range(3, 81, 9)),
    list(range(4, 81, 9)),
    list(range(5, 81, 9)),
    list(range(6, 81, 9)),
    list(range(7, 81, 9)),
    list(range(8, 81, 9))
]

# indices associated with each box (3x3 sub-grid)
BOXES = [
    [0, 1, 2,  9, 10, 11, 18, 19, 20],
    [3, 4, 5, 12, 13, 14, 21, 22, 23],
    [6, 7, 8, 15, 16, 17, 24, 25, 26],

    [27, 28, 29, 36, 37, 38, 45, 46, 47],
    [30, 31, 32, 39, 40, 41, 48, 49, 50],
    [33, 34, 35, 42, 43, 44, 51, 52, 53],

    [54, 55, 56, 63, 64, 65, 72, 73, 74],
    [57, 58, 59, 66, 67, 68, 75, 76, 77],
    [60, 61, 62, 69, 70, 71, 78, 79, 80]
]