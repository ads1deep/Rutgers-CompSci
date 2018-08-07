class C:
    def __init__(self, lastname):
        self.lname = lastname

class A:
    x = 2
    y = 5
    def __init__(self, initnum = 0, lastname = ""):
        self.num = initnum
        self.lname = lastname
    def method1(self, inc):
        self.num += inc
    def __str__(self):
        return "Number: " + str(self.num) + "; Name: " + self.lname
    def __repr__(self):
       return str(self) # self.__str__()
    
    

