import math as m
print('Добро пожаловать в калькулятор! Приятной работы!')
x = input('Первая переменная: ')
y = input('Вторая переменная: ')
z = input('Действие: ')

if x == 'pi':
    x = m.pi
elif x == 'e':
    x = m.e
else: 
    x = int(x)   

if y == 'pi':
    y = m.pi
elif y == 'e':
    y = m.e
else: 
    y = int(y)

if z == '+'
