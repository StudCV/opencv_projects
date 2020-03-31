from math import pi, e

num1 = input ("Введите первое число:")
if num1 == "pi":
    num1 = pi
if num1 == 'e':
    num1 = e
num2 = input ("Введите второе число:")
if num2 == 'pi':
    num2 = pi
if num2 == 'e':
    num2 = e
x = float(num1)
y = float(num2)
op = input ("""
    Выберите операцию:
    + сложение
    - вычитание
    * умножение
    / деление
    % деление по модулую
    ** возведение в степень 
    """)
if op == '+':
    print('Ответ:', x+y)
elif op == '-':
    print('Ответ:', x-y)
elif op == '*':
    print('Ответ:', x*y)
elif (op == '/' and y == 0):
    print("Деление на ноль!")
elif op == '/':
    print('Ответ:', x/y)
elif (op == '%' and y == 0):
    print("Деление на ноль!")
elif op == '%':
    print('Ответ:', x%y)
elif op == '**':
    print('Ответ:', x**y)
else :
    print ("Выбрана некорректная операция! Повторите попытку")
