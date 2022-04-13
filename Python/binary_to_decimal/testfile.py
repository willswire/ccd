# Refer to README.md for the problem instructions


def binary_to_decimal(binaryNumber):
    if not(isBinary(binaryNumber)):
        return "Invalid Input"
    else:
        return convert(binaryNumber)

def convert(binaryNumber):
    inputString = str(binaryNumber)
    stringLength = len(inputString)
    res = 0
    pos = 1
    for x in inputString:
        if (x == "1"):
            res += pow(2, (stringLength - pos))
        pos += 1
    return res

def isBinary(input):
    inputSet = set(str(input))
    binarySetA = {'1', '0'}
    binarySetB = {'1'}
    binarySetC = {'0'}

    return (inputSet == binarySetA or inputSet == binarySetB or inputSet == binarySetC)