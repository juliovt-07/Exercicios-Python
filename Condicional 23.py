#Determine se um determinado ano lido é bissexto.
#Sendo que um ano é bissexto se for divisível
#por 400 ou se for divisível por 4 e não for divisível por 100.
#Por exemplo: 1988, 1992, 1996
ano = int(input("Informe o Ano: "))
d1, d2= 0,0
if ano%4 > 0:
    d1 = 1
if ano%100 == 0:
    d2 = 1
if (d1+d2) == 0:
    print("{} é um ano bissexto!".format(ano))
else:
    print("{} não é um ano bissexto!".format(ano))
