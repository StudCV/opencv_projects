import math as m
import os
os.system('clear')
while True:
    a = input('Введите первое число: ')
    try:
        if a == 'pi':
            a = m.pi
        elif a == 'e':
            a = m.e
        else:
            a = float(a)
    except ValueError:
            print('Введите число или pi, или e')
            continue
    b = input('Введите второе число: ')
    try:
        if b == 'pi':
            b = m.pi
        elif b == 'e':
            b = m.e
        else:
            b = float(b)
    except ValueError:
            print('Введите число или pi, или e')
            continue

    c = input('Введите действие: ')
    
    if c == '+':
        print(a, ' + ', b,  ' = ', a + b)
    elif c == '-':
        print(a, ' - ', b,  ' = ', a - b)
    elif c == '*':
        print(a, ' * ', b,  ' = ', a * b)
    elif c == '/':
        try:
            print(a, ' / ', b,  ' = ', a / b)
        except ZeroDivisionError:
            print('Деление на ноль')
            continue
    elif c == '^':
        print(a, ' ^ ', b,  ' = ', a ** b)
    elif c == '%':
        try:
            print(a, ' \%\ ', b,  ' = ', a % b)
        except ZeroDivisionError:
            print('Деление на ноль')
            continue
    d = input('Хотите продолжить Да(1)/Нет(2): ')
    if d == '1':
        pass
    elif d == '2':
        break
    os.system('clear')