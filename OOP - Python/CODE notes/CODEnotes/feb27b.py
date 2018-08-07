class C:
    def __init__(self, lastname = ""):
        self.lname = lastname
    def __str__(self):
        return str(self.lname)
    def __repr__(self):
        return "some string"
    def changename(self, lastname):
        self.lname = lastname
    def printname(self):
        print(self.lname)
