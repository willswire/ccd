# Refer to README.md for the problem instructions


def convertAndShift(bStr):
    if not(validateLength(bStr)):
        return "INVALID_LENGTH"
    elif not(validateContents(bStr)):
        return "INVALID_VALUE"
    else:
        val = convert(bStr)
        if (val % 2 == 0):
            val <<= 2
        else:
            val >>= 1
        
        if (val > 200):
            return ~ val
        else:
            return val
        

def convert(string):
    res = 0
    pos = 1
    size = len(string)
    for x in string:
        if (x == "1"):
            res += pow(2, (size - pos))
        pos += 1
    return res

def validateLength(input):
    return len(input) == 16

def validateContents(input):
    inputSet = set(input)
    binSetA = { '1', '0'}
    binSetB = { '1' }
    binSetC = { '0' }

    return (inputSet == binSetA or inputSet == binSetB or inputSet == binSetC)