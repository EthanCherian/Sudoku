from grid import Grid
from helpers import convertUserInput

grid = Grid()
while True:
    print(grid)

    idxInput = input("Where would you like to enter a digit? (e.g. 'A3', 'D9', 'I1') ")
    try:
        idx = convertUserInput(idxInput)
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    digInput = input("Which digit would you like to place there? (1-9, or -1 to cancel) ")
    digit = 0
    try: 
        digit = int(digInput)
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
    if digit == -1:
        print("Cancelling...")
        continue

    grid.placeDigit(idx, digit)