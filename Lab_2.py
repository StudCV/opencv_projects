import math
x=input("Первый операнд: ")
if x == "e":
    x = math.e
elif x == "pi":
    x = math.pi
else:
    x = float(x)
y=input("Второй операнд: ")
if y == "e":
    y = math.e
elif y == "pi":
    y = math.pi
else:
    y = float(y)
oper=input("Операция: ")
if oper == "+":
    print(x+y)
elif oper == "-":
    print(x-y)
elif oper == "*":
    print(x*y)
elif oper == "/":
    if y == 0:
        print("Ошибка, деление на ноль")
    else: 
        print(x/y)
elif oper == "%":
    if y == 0:
        print("Ошибка, деление на ноль")
    else: 
        print(x%y)
elif oper == "**":
    if (x > 1) and (y > 600):
        x = int(x)
        y = int(y)
    print(x**y)
