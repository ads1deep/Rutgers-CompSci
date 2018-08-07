a = 2
b = 4
c = 6

def someFun(a, b):
    a = a + b
    b = a + c
    print(a, b, c)

someFun(a, b) 
print(a, b, c)
someFun(b, c) 
print(a, b, c)

