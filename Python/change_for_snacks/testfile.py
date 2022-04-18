# Refer to README.md for the problem instructions


def computeChange(change):
    COST_FRIES = 1.50
    COST_SODA = 1.00
    ammount = 0

    for value in change.values():
        if value < 0:
            return 0

    for key in change.keys():
        if key == "H":
                ammount += change["H"] * .50
        elif key == "Q":
                ammount += change["Q"] * .25
        elif key == "D":
                ammount += change["D"] * .10
        elif key == "N":
                ammount += change["N"] * .05
        elif key == "P":
                ammount += change["P"] * .01

    ammount = round(ammount, 2)

    if (ammount >= COST_FRIES + COST_SODA):
        return ammount, 'BOTH'
    elif (ammount >= COST_FRIES):
        return ammount, 'FRIES'
    elif (ammount >= COST_SODA):
        return ammount, 'SODA'
    else:
        return ammount, 'NOTHING'
