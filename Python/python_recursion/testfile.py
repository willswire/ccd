# Refer to README.md for the problem instructions


def createOrderedList(uList):
    if len(uList) == 0:
        return uList

    for i in range(len(uList)):
        for j in range(len(uList) - i - 1):
            if uList[j] > uList[j + 1]:
                uList[j], uList[j + 1] = uList[j + 1], uList[j]
    
    return uList                


def binarySearch (lst, start, end, val):
    if (len(lst) == 0):
        return -2
    
    if end >= start:

        middle = (end + start) // 2

        if (val == lst[middle]):
            return middle
        elif (val < lst[middle]):
            return binarySearch(lst, start, middle - 1, val)
        elif (val > lst[middle]):
            return binarySearch(lst, middle + 1, end, val)
            
    else:
        return -1 
