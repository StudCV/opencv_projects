import math
from math import e, pi

a=input('Enter first number: ')
x1=float(a)
b=input('What action? ')
x3=int(b)
c=input('Enter second number: ')
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
    else
        print(str(x1),'/',str(x2),'=',str(x1/x2))
elif x3 == 4:
    print(str(x1),'%',str(x2),'=',str(x1%x2))
elif x3 == 5:
    print(str(x1),'^',str(x2),'=',str(x1**x2))
else 
    print('Youre wrong')

