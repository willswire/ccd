# Refer to README.md for the problem instructions


def create_file(names):
    if (len(names) != 0):
        try:
            for name in names:
                if (len(name) != 2 or name[0] == "" or name[1] == ""):
                    raise ValueError()
                name[0] = name[0].title()
                name[1] = name[1].title()
            names.sort(key= lambda name : name[1])
        except:
            return 'INVALID_NAME'
    else:
        return 'EMPTY_LIST'

    try:
        with open('names.txt', 'w') as f:
            for name in names:
                line = name[1] + ", " + name[0]
                f.write(line)
                f.write('\n')
    except:
        return 'FILE_ERROR'

    return 'SUCCESS'
