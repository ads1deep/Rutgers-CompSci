
# Another example to illustrate LEGB scope rules

x = "green"

def f():
    def nested():
        x = "eggs"
        print(x, len(x)) 
    nested()
    print(x) 

# print(x)
