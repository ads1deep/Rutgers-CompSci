def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

class Fraction:
    def __init__(self, init_num = 0, init_den = 1):
        if init_den == 0:
            raise Exception("Error: zero denominator")
        if init_den < 0:
            init_num *= -1
            init_den *= -1
        g = gcd(abs(init_num), abs(init_den))
        self.num = init_num//g
        self.den = init_den//g

    def __str__(self):
        return "%d/%d"%(self.num, self.den)

    def __repr__(self):
        return "%d/%d"%(self.num, self.den)
        # return self.__str__(), or str(self)

    def reciprocal(self):
        return Fraction(self.den, self.num) #creates a Fraction object (calls the constructor)

    def invert(self):
        g = self.reciprocal()
        self.num = g.num
        self.den = g.den

    def __add__(self, other):
        return Fraction(self.num * other.den + self.den * other.num, self.den * other.den)

    def __sub__(self, other):
        return Fraction(self.num * other.den - self.den * other.num, self.den * other.den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return self * other.reciprocal()

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not (self == other)

    

    

        
        
