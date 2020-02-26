a,s,b = input("Введите операнды в формате 'первый операнд|операция|второй операнд':").split()

'''
определяем: была ли введена константа
'''
def pars(x):
    length=len(x)
    if length < 3:
        if x=="e":
            from math import e as x
            return x
        elif x=="pi":
            from math import pi as x
            return x
    return float(x)

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
