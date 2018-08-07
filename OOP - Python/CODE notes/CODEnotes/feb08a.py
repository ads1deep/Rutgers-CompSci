
# An example to illustrate the use of 'global'

# Note that if a name declared to be global 
# in a function does not already exist in the 
# global namespace, it will be created in the 
# global namespace by the assignment statement. 
# Comment out the first and last lines of code 
# in this module to see this.

# x = "green"

def f():
    x = "ham"
    def nested():
        global x
        # x = "eggs"
        print(x)
    nested()
    print(x)

# print(x)
