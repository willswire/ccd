class Computer:
    def __init__(self, brand, model, cost, ram, storage):
        self.brand = brand
        self.model = model
        self.cost = cost
        self.ramGB = ram
        self.storageGB = storage
    # BELOW FUNCTION NOT NEEDED FOR SOLUTION - method only used in test cases to check if two objects are equal
    
    def __eq__(self, other): 
        return self.brand == other.brand and self.model == other.model and \
        self.cost == other.cost and self.ramGB == other.ramGB and self.storageGB == other.storageGB
