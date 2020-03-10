import math
from math import e, pi

while True:
    a=input('Enter first number: ')
    if a=='pi':
        x1=pi
    elif a=='e':
        x1=e
    else: x1=float(a)
    b=input('What action?\nSum:\n      1\nSubtract: 2\nMultiply: 3\nDivide:   4\nModule:   5\nPower:    6\n')
    x3=int(b)
    c=input('Enter second number: ')
    if c=='pi':
        x2=pi
    elif c=='e':
        x2=e    
    else: 
        x2=float(c)
    if x3 == 1:
        print(str(x1),'+',str(x2),'=',str(x1+x2))
    elif x3 == 2:
        print(str(x1),'-',str(x2),'=',str(x1-x2))
    elif x3 == 3:
        print(str(x1),'*',str(x2),'=',str(x1*x2))
    elif x3 == 4:
        if x2 == 0:
            print('Youre wrong')
        else:
            print(str(x1),'/',str(x2),'=',str(x1/x2))
    elif x3 == 5:
        print(str(x1),'%',str(x2),'=',str(x1%x2))
    elif x3 == 6:
        print(str(x1),'^',str(x2),'=',str(x1**x2))
    else: 
        print('Youre wrong')
    d = input('Хотите продолжить?\nДа   1\nНет  2: ')
    if d == '1':
        pass
    elif d == '2':
        break

