#Usando switch, escreva um programa que leia um inteiro entre 1 e 12
#e imprima o mês correspondente a este numero. Isto é, janeiro se 1,
#fevereiro se 2, e assim por diante.
mes = int(input("Número de 1 a 12: "))
if mes <= 0 & mes > 12:
    print("Número Inválido")
elif mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosta")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")