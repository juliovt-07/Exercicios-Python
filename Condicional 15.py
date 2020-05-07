#Usando switch, escreva um programa que leia um inteiro entre 1 e 7
#e imprima o dia da semana correspondente a este numero.
#Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
n = int(input("Escolha de 1 a 7: "))
if n == 0:
    print("Número Inválido ")
elif n == 1:
    print("Domingo")
elif n == 2:
    print("Segunda")
elif n == 3:
    print("Terça")
elif n == 4:
    print("Quarta")
elif n == 5:
    print("Quinta")
elif n == 6:
    print("Sexta")
elif n == 7:
    print("Sábado")
