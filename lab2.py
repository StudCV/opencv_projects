import math as m
a = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Введите действие: ')
if a == 'pi':
    a = m.pi
elif a == 'e':
    a = m.e
else:
    a = float(a)
if b == 'pi':
    b = m.pi
elif b == 'e':
    b = m.e
else:
    b = float(b)

if c == '+':
    print('a + b =', a + b)
elif c == '-':
    print('a - b =', a - b)
elif c == '*':
    print('a * b =', a * b)
elif c == '/':
    print('a / b =', a / b)
elif c == '^':
    print('a ^ b =', a ** b)
elif c == '%':
    print('a \%\ b =', a % b)    