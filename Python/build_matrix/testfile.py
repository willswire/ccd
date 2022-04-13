# Refer to README.md for the problem instructions


def buildMatrix(rows, cols):
    res = []
    if validateMatrix(rows, cols):
        res = [[0 for i in range(cols)] for j in range(rows)]
        for row in range(rows):
            for column in range(cols):
                res[row][column] = row * column
        if (rows == cols) and (rows % 2 == 1):
            center = int(rows / 2)
            res[center][center] = 1
    print(res)
    return res

def validateMatrix(rows, cols):
    return (rows > 1) and (cols > 1)