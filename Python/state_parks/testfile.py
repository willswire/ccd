# Refer to README.md for the problem instructions


def find_parks(parkList, state):

    if parkList == None or len(parkList) == 0 or state == None or len(state) == 0:
        return "INVALID_DATA"

    parks = set()
    for park in parkList:
        try:
            if park["cost"] < 8:
                return "INVALID_DATA"
            elif park["cost"] < 15:
                fStateA = park["state"].lower()
                fStateB = state.lower()
                if fStateA == fStateB:
                    parks.add(park["park"])
        except:
            return "KEY_ERROR"

    return parks
