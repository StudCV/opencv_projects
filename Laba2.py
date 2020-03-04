from math import e
from math import pi as p
x = input("Введите 1-е число: ")
if (x == "Pi" or x == "pi" or x == "PI"):
  x = p
if (x == "E" or x == "e" ):
  x = e
y = input("Введите 2-е число: ")
if (y == "Pi" or y == "pi" or y == "PI"):
  y = p
if (y == "E" or y == "e" ):
  y = e
num1 = x
num1 = float (num1)
num2 = y
num2 = float (num2)
y = float (y)
print("Введите операцию ")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Деление по модулю")
print("6. Возведение в степень")
print("7. Выход")
choice = int(input("Введите желаемую операцию  "))
if (choice >= 1 and choice <= 6):
  if choice == 1:
      res = num1 + num2
      print("Результат = ", res)
  elif choice ==2:
      res = num1 - num2
      print("Результат = ", res)
  elif choice ==3:
      res = num1 * num2
      print("Результат = ", res)
  elif (choice == 4 and num2 == 0):
      print("Деление на ноль")
  elif (choice == 4 and num2 > 0): 
      res = num1 / num2
      print("Результат = ", res)
  elif choice == 5:
      res = num1 % num2
      print("Результат = ", res)
  elif choice == 6:
      res = num1 ** num2
      print("Результат = ", res)
else: 
  print("До свидания )0))") 
