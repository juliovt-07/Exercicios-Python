#Faça um programa que receba a altura e o peso de uma pessoa.
#De acordo com a tabela a seguir, verifique e mostra qual a
#classificação dessa pessoa.
escolha = ord("s")
while escolha == 115 or escolha == 83:
    try:
        alt = float(input("Altura: "))
    except ValueError as err:
        print("É a altura, DOENTE!")
    try:
        peso = int(input("Peso: "))
    except ValueError as err:
        print("É o peso, DOENTE!")
    if alt < 0:
        print("Altura Inválida")
    elif alt < 1.20:
        if peso < 0:
            print("Peso Inválido")
        elif peso <= 60:
            print("Classificação: [ A ]")
        elif peso > 60 and peso <= 90:
            print("Classificação: [ D ]")
        elif peso > 90:
            print("Classificação: [ G ]")
        escolha = str(input("Repetir? s / n : "))
        escolha = ord(escolha)
    elif alt >= 1.20 and alt <= 1.70:
        if peso < 0:
            print("Peso Inválido")
        elif peso <= 60:
            print("Classificação: [ B ]")
        elif peso > 60 and peso <= 90:
            print("Classificação: [ E ]")
        elif peso > 90:
            print("Classificação: [ H ]")
        escolha = str(input("Repetir? s / n : "))
        escolha = ord(escolha)
    elif alt > 1.70:
        if peso < 0:
            print("Peso Inválido")
        elif peso <= 60:
            print("Classificação: [ C ]")
        elif peso > 60 and peso <= 90:
            print("Classificação: [ F ]")
        elif peso > 90:
            print("Classificação: [ I ]")
        escolha = str(input("Repetir? s / n : "))
        escolha = ord(escolha)
    alt = 0
    peso = 0
print("Tchau, Obrigado!")