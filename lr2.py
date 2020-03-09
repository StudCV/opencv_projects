from math import e, pi

def verify_input(x, i):
    if x[i] == "e" :
        elem = e
    elif x[i] == "pi" :
        elem = pi
    else :
        elem = x[i]
    return elem

def calc_elements(a, b, delim) :
    if delim == "+" :
        res = a + b
    elif delim == "-" :
        res = a - b
    elif delim == "*" :
        res = a * b
    elif delim == "/" :
        try:
            res = a / b
        except ZeroDivisionError:
            res = "Dividing on zero error"
    elif delim == "%" :
        try:
            res = a % b
        except ZeroDivisionError:
            res = "Dividing on zero error"
    elif delim == "^" :
        res = a ** b
    return res

print("Welcome to Calculator")
a = 0   # 1 operand init
b = 0   # 2 operand init

str = input("Enter expression:\n")
while str != "q" :
    x = str.split()
    
    a = verify_input(x, 0)      # checking 1 operand
    a = float(a)
    b = verify_input(x, 2)      # checking 2 operand
    b = float(b)

    delim = x[1]                # checking the operator
    res = calc_elements(a, b, delim)  # calculation depends on delim (operand)
    print(res)
    str = input("Enter expression:\n")


    