from grid import Grid
from helpers import convertUserInput

rem = int(input("How many digits should be removed? (1-81) "))
grid = Grid(md=rem)

while not grid.isComplete():
    print(grid)

    idxInput = input("Where would you like to enter a digit? (e.g. 'A3', 'D9', 'I1', or -1 to exit) ")
    if idxInput == "-1":
        print("Exiting...")
        break
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

    if grid.isValidMove(idx, digit):
        grid.placeDigit(idx, digit)
    else:
        print("\t**** Invalid move ****")

print("You win!")