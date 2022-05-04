# Refer to README.md for the problem instructions


def count_unique_permutations(input_str):
    print("Checking for: ", input_str)

    res = {input_str}

    for k in range(len(input_str)):
        strList = list(input_str)[k:]
        for i in range(len(strList)):
            for j in range(len(strList) - 1):
                strList[j], strList[j + 1] = strList[j + 1], strList[j]
                string = "".join(strList)
                prefix = "".join(strList[:k])
                print(prefix + string)
                res.add(prefix + string)

    print(res)

    return len(res)
