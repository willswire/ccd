# Refer to README.md for the problem instructions


def classify_shapes(shapeList):

    if shapeList == None or len(shapeList) == 0:
        return "EMPTY_LIST"

    shapeDict = {
        "triRight": 0,
        "triEquilateral": 0,
        "triOther": 0,
        "triInvalid": 0,
    }

    for shape in shapeList:
        if len(shape) != 3:
            return "INVALID_LIST"
        angleA = shape[0]
        angleB = shape[1]
        angleC = shape[2]

        if angleA + angleB + angleC != 180:
            shapeDict["triInvalid"] += 1
        elif (
            (angleA not in range(1, 179))
            or (angleB not in range(1, 179))
            or (angleC not in range(1, 179))
        ):
            shapeDict["triInvalid"] += 1
        elif angleA == 90 or angleB == 90 or angleC == 90:
            shapeDict["triRight"] += 1
        elif angleA == 60 and angleB == 60 and angleC == 60:
            shapeDict["triEquilateral"] += 1
        else:
            shapeDict["triOther"] += 1

    return shapeDict
