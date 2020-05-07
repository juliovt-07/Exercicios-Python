#Leia uma data e determine se ela é válida. Ou seja, verifique se
#o mês está entre 1 e 12, e se o dia existe naquele mês.
#Note que Fevereiro tem 29 dias em anos bissextos,
#e 28 dias em anos não bissextos.
data = str(input("Insira um data (sem barras):\nEx: 07022007\n---> "))
dia = [data[0]+data[1]]
d = int(dia[0])
mes = [data[2]+data[3]]
m = int(mes[0])
ano = [data[4]+data[5]+data[6]+data[7]]
a = int(ano[0])
b = False
valido = bool
ok = True
dat = ("{}/{}/{}".format(dia[0],mes[0],ano[0]))
while ok == True:
    if a < 1000 or a > 9999:
        valido = False
        ok = False
    elif a%400 == 0:
        b = True
        ok = False
    elif a%4 == 0:
        b = True
        ok = False
    elif a%100 == 0:
        b = False
    if m <= 0 or m > 12:
        valido = False
        ok = False
    elif b == True and m == 2:
        if d > 0 and d <= 29:
            valido = True
        else:
            valido = False
            ok = False
    elif b == False and m == 2:
        if d == 29:
            valido = False
            ok = False
    elif d > 0 and d <= 31:
        valido = True
        ok = False
if valido == True:
    print("{} é uma data válida".format(dat))
else:
    print("{} não é uma data válida".format(dat))