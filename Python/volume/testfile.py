# Refer to README.md for the problem instructions
import math

def computeVolume(item1, item2):
    sParam = None
    cParam = None

    if (type(item2) is list):
        sParam = item1
        cParam = item2
    else:
        sParam = item2
        cParam = item1

    try:
        if not(sParam > 0):
            return 'INVALID'
        if not(cParam[0] > 0 and cParam[1] > 0 and cParam[2] > 0):
            return 'INVALID'
    except:
        return 'INVALID'

    sVol = round(4/3 * math.pi * math.pow(sParam, 3))
    cVol = cParam[0] * cParam[1] * cParam[2]

    return sVol + cVol
