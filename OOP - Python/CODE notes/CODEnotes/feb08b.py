# An example to illustrate the use of nonlocal

def f():
    x = "green"
    def nested():
        nonlocal x
        x = "eggs"
        print(x)
    nested()
    print(x)

