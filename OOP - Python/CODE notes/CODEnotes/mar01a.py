class ThreeInts:
    def __init__(self, init_a = 0, init_b = 0, init_c = 0):
        self.a = init_a
        self.b = init_b
        self.c = init_c
    def __str__(self):
        return str(self.a) + "__" + str(self.b) + "__" + str(self.c)
    def __repr__(self):
        return str(self)
    def __add__(self, other):
        return ThreeInts(self.a + other.a, self.b + other.b, self.c + other.c)
    def __sub__(self, other):
        return ThreeInts(self.a - other.a, self.b - other.b, self.c - other.c)
    def __mul__(self, other):
        return ThreeInts(self.a * other.a, self.b * other.b, self.c * other.c)
    def __truediv__(self, other):
        return ThreeInts(self.a // other, self.b // other, self.c // other)
    
    
    
