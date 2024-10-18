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