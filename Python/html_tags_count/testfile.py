# Refer to README.md for the problem instructions


def HTML_count_tags(hString):
    result = []
    currentLevel = -1
    deepestLevel = currentLevel
    for i in range(len(hString) - 1):

        if hString[i] == '<' and hString[i + 1] != '/':
            result.append(0)
            currentLevel += 1
            result[currentLevel] += 1
        elif hString[i + 1] == '/':
            currentLevel -= 1

        if currentLevel > deepestLevel:
            deepestLevel += 1
        

    return result[slice(deepestLevel + 1)]
