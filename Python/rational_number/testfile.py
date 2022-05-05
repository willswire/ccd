# Refer to README.md for the problem instructions


class RationalNumber:
    def __init__(self, top = 0, bottom = 1):
        """
        create a RationalNumber by providing a numerator and denominator
        """
        if (bottom == 0):
            raise ValueError("Cannot divide by zero")

        a = top
        b = bottom
        while b:
            a, b = b, a % b
        gcd = a

        self.top = int(top / gcd)
        self.bottom = int(bottom / gcd)

    def add(self, number):
        """
        return the sum of the current RationalNumber and another
        """
        newTop = (self.top * number.bottom) + (number.top * self.bottom)
        newBottom = (self.bottom * number.bottom)
        return RationalNumber(newTop, newBottom)

    def subtract(self, number):
        """
        return the difference of the current RationalNumber and another
        """
        newTop = (self.top * number.bottom) - (number.top * self.bottom)
        newBottom = (self.bottom * number.bottom)
        return RationalNumber(newTop, newBottom)

    def multiply(self, number):
        """
        return the product of the current RationalNumber and another
        """
        newTop = self.top * number.top
        newBottom = self.bottom * number.bottom
        return RationalNumber(newTop, newBottom)

    def divide(self, number):
        """
        return the quotient of the current RationalNumber and another
        """
        newTop = self.top * number.bottom
        newBottom = self.bottom * number.top
        return RationalNumber(newTop, newBottom)
    
    def printFraction(self):
        """
        return the RationalNumber in fraction format
        """
        return str(self.top) + "/" + str(self.bottom)

    def printDecimal(self):
        """
        return the RationalNumber in decmial format
        """
        return round(self.top / self.bottom, 2)