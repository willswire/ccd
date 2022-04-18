import math

# Refer to README.md for the problem instructions

class Player(object):
    name: str
    health: float
    x_pos: float
    y_pos: float

    def __init__(self, name, health = 100.0, x_pos = 0.0, y_pos = 0.0):
        self.name = name
        self.health = health
        self.x_pos = x_pos
        self.y_pos = y_pos

    def report_pos(self):
        return self.x_pos, self.y_pos

    def reduce_health(self, dmg):
        self.health -= dmg / 2
        if (self.health < 0.0):
            self.health = 0.0
    
    def move(self, x_pos, y_pos):
        self.x_pos += x_pos
        self.y_pos += y_pos

        if (y_pos < 0 and abs(y_pos) >= 5):
            amt = (x_pos * x_pos) + (y_pos * y_pos)
            self.reduce_health(math.sqrt(amt))
        if (self.health == 0):
            print("You are out of hit points!")
        

        return self.health
    
