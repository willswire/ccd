# Refer to README.md for the problem instructions
from supportClass import Computer

def create_computer_objects(fileName):
    lines = []
    try:
        with open(fileName) as file:
            for line in file:
                lines.append(line)
    except:
        raise FileNotFoundError("FILE CORRUPTED")

    computerObjects = []
    try:
        for line in lines:
            splitLine = line.split(', ')
            brand = str(splitLine[0])
            model = str(splitLine[1])
            cost = float(splitLine[2])
            ram = int(splitLine[3])
            storage = int(splitLine[4])

            if (brand != 'Asus' and cost > 500 and cost < 1000 and ram >= 8):
                computerObjects.append(Computer(brand, model, cost, ram, storage))
    except:
        raise ValueError("INVALID DATA")

    return computerObjects
