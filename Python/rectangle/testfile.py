# Refer to README.md for the problem instructions


class Rectangle:

    def __init__(self, upperLeft, lowerRight):
        """
        create a Rectangle by providing two tuple sets of coordinates
        """
        if (upperLeft[0] < 0 or upperLeft[1] < 0 or lowerRight[0] < 0 or lowerRight[1] < 0):
            raise ValueError("The coordinates provided are not in the first quadrant")
        else:
            self.upperLeft = upperLeft
            self.lowerRight = lowerRight
        pass

    def length(self):
        """
        return the length (y-axis distance) of the Rectangle
        """
        return self.upperLeft[1] - self.lowerRight[1]

    def width(self):
        """
        return the width (x-axis distance) of the Rectangle
        """
        return self.lowerRight[0] - self.upperLeft[0]
    
    def perimeter(self):
        """
        return the perimeter (x-axis and y-axis distances) of the Rectangle
        """
        return (2 * self.length()) + (2 * self.width())

    def area(self):
        """
        return the area enclosed by the Rectangle
        """
        return self.length() * self.width()
    
    def isSquare(self):
        """
        return True if the rectangle's length and width are equal
        """
        return self.length() == self.width()