a,s,b = input("Введите операнды в формате 'первый операнд|операция|второй операнд':").split()

'''
определяем: была ли введена константа
'''
def pars(a):
    length=len(a)
    if length < 3:
        if a=="e":
            from math import e as a
            return a
        elif a=="pi":
            from math import pi as a
            return a
    return int(a)

if s=="+":
    print(str(a)+"+"+str(b)+"="+str('%.2f' % (pars(a)+pars(b))))
    #print(f"{a}+{b}={pars(a)+pars(b)}")
elif s=="-":
    print(str(a)+"-"+str(b)+"="+str('%.2f' % (pars(a)-pars(b))))
elif s=="*":
    print(str(a)+"*"+str(b)+"="+str('%.2f' % (pars(a)*pars(b))))
elif s=="/":
    print(str(a)+"/"+str(b)+"="+str('%.2f' % (pars(a)/pars(b))))
elif s=="%":
    print(str(a)+"%"+str(b)+"="+str('%.2f' % (pars(a)%pars(b))))
elif s=="**":
    print(str(a)+"**"+str(b)+"="+str('%.2f' % (pars(a)**pars(b))))
else:
    print("неверная операция")