import math
from math import e, pi

a=input('Enter first number: ')
if a=='pi':
    x1=pi
elif a=='e':
    x1=e
else: x1=float(a)
b=input('What action?
        Sum:      1
        Subtract: 2
        Multiply: 3
        Divide:   4
        Module:   5
        Power:    6')
x3=int(b)
c=input('Enter second number: ')
if a=='pi':
    x2=pi
elif a=='e':
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
    if x2 == 0
        print('Youre wrong')
    else:
        print(str(x1),'/',str(x2),'=',str(x1/x2))
elif x3 == 5:
    print(str(x1),'%',str(x2),'=',str(x1%x2))
elif x3 == 6:
    print(str(x1),'^',str(x2),'=',str(x1**x2))
else: 
    print('Youre wrong')

