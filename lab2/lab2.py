from math import pi, e

x,op,y = input("Enter the expression: \n").split()
if x == "pi":
    x = pi
elif x == "e":
    x = e
else:
    x = float(x)
if y == "pi":
    y = pi
elif y == "e":
    y = e
else:
    y = float(y)

if op == "+":
    z = x + y
elif op == "-":
    z = x - y
elif op == "*":
    z = x * y
elif op == "/":
    if y == 0:
        print("Divide by 0 is impossible")
        z = None
    else:
        z = x / y
elif op == "%":
    if y == 0:
        print("Divide by 0 is impossible")
        z = None
    else:
        z = x%y
elif op == "**":
    z = x**y
elif op == "==":
    if x == y:
        print("Numbers are equal")
        z = None
    else:
        print("Numbers aren't equal")
        z = None
if z != None:
    print("Result:", z)