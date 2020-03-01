import math
while True:
    def is_number(x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def check(x):
        if is_number(x) == True:
            return(x)
        elif is_number(x) == False:
            if x == "pi":
                x = math.pi;
            elif x == "e":
                x = math.e;
            else:
                print("ошибка:введите число");
                return False
        return(x)

    while True:
        x1 = input("введите первое число: ");
        if check(x1)!=False:
            x1=float(check(x1));
            break

    while True: #цикл каждый раз проверяется
        x2 = input("введите второе число: ");
        if check(x2) != False:
            x2 = float(check(x2));
            break

    while True:
        print("Действия:");
        print("1.сложение");
        print("2.вычитание");
        print("3.умножение");
        print("4.деление");
        print("5.деление по модулю");
        print("6.возведение в степень");
        print("7.сравнение");

        act = input("Выберите действие: ");
        act = int(act);

        if 0 < act < 8:
            if act == 1:
                y = x1 + x2;  # сложение
            elif act == 2:
                y = x1 - x2;  # вычитание
            elif act == 3:
                y = x1 * x2;  # умножение
            elif act == 4:
                if x2!=0:
                    y = x1 / x2;  # деление
                    break
                elif x2==0:
                    print("");
                    print("нельзя делить на ноль! Выберите другое действие.");
                    print("");
            elif act == 5:
                if x2 != 0:
                    y = x1 % x2;  # деление по модулю
                    break
                elif x2 == 0:
                    print("");
                    print("нельзя делить на ноль! Выберите другое действие.");
                    print("");
            elif act == 6:
                y = x1 ** x2;  # возведение в степень
            elif act == 7:
                y = x1 == x2;  # сравнение

            if(act!=4 and act!=5):
                break

        # ответ
    print("Ответ: ", y);
    while True:
        cont=input("Желаете продолжить [Y/N]: ");
        if cont=="Y":
            break
        elif cont!="Y" and cont!="N":
            print("попробуйте снова")
        else:
            break
    if cont=="N":
        break
