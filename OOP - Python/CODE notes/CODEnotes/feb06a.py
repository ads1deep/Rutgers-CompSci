# An example to illustrate LEGB scope rules

x = "green"

def f():
    x = "eggs"
    def nested():
        x = "ham"
        print(x)
    nested()
    print(x)

print(x)
