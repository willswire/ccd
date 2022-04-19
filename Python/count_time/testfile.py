# Refer to README.md for the problem instructions


def find_culprits(fileName):
    lines = []
    try:
        with open(fileName) as file:
            for line in file:
                lines.append(line)
    except:
        return None

    users = {}
    for line in lines:
        splitLine = line.split(", ")
        key = str(splitLine[0])
        value = int(splitLine[1])
        if key in users:
            curVal = users[key]
            users.update({key: curVal + value})
        else:
            users[key] = value

    userList = []
    for key in users:
        userList.append([key, users[key]])
    
    userList.sort(key=lambda x: x[1], reverse=True)
    topFive = slice(5)
    return userList[topFive]
