L = [lambda x: x*x, lambda x: x**3, lambda x: x**4]
choice = int(input("Enter 0, 1, 2 for square, cube, fourth power: "))
num = int(input("Enter an integer: "))
print("Your answer is: ", L[choice](num))

