from math import pi,e
op = input ("""
    Выберите операцию:
    + сложение
    - вычитание
    * умножение
    / деление
    % деление по модулую
    ** возведение в степень
    == сравнение 
    """)
num1 = input ("Введите первое число:")
num2 = input ("Введите второе число:")
x = int(num1)
y = int(num2)
if op == '+':
    print('Ответ:',x+y)
elif op == '-':
    print('Ответ:',x-y)
elif op == '*':
    print('Ответ:',x*y)
elif op == '/':
    print('Ответ:',x/y)
elif op == '%':
    print(x%y)
elif op == '**':
    print('Ответ:',x**y)
elif op == '==':
    print('Ответ:',x==y)
else: 
    print ('Ошибка! Ввыедите один из предложенных операторов')
