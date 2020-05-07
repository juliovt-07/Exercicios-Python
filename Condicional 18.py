#programa que mostre ao usuário um menu com 4 opções de operações matemáticas
#(as básicas, por exemplo). O usuário escolhe uma das opções
#e o seu programa então pede dois valores
#numéricos e realiza a operação, mostrando o resultado e saindo.
escolha = 1
while escolha < 5 or escolha >= 6:
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("'1' Soma: ")
    print("'2' Multiplicação: ")
    print("'3' Subtração: ")
    print("'4' Divisão: ")
    try:
        escolha = int(input("Escolha uma opção de 1 a 4 ('5' para Sair): "))
    except ValueError as err:
        print('Formato Errado')
        escolha = 0
    if escolha <= 0 or escolha > 5:
        print("Opção Inválida!")
    elif escolha == 1:
        print("||||||||||||||||||||||||||||||||||||||||||||||||\nSoma:\n... ")
        try:
            n1 = int(input("Primeiro Valor: "))
        except ValueError as err:
            escolha = 0
            print("Formato Errado")
        try:
            n2 = int(input("Segundo Valor: "))
        except ValueError as err:
            escolha = 0
            print("Formato Errado")
        if escolha > 0:
            print("{} + {} = {}".format(n1,n2,(n1+n2)))
    elif escolha == 2:
        print("||||||||||||||||||||||||||||||||||||||||||||||||\nMultiplicação:\n... ")
        try:
            n1 = int(input("Valor Multiplicado: "))
        except ValueError as err:
            escolha = 0
            print("Formato Errado")
        try:
            n2 = int(input("Multiplicador: "))
        except ValueError as err:
            escolha = 0
            print("Formato errado")
        if escolha > 0:
            print("{} x {} = {}".format(n1,n2,(n1*n2)))
    elif escolha == 3:
        print("||||||||||||||||||||||||||||||||||||||||||||||||\nSubtração:\n")
        try:
            n1 = int(input("Valor Subtraído: "))
        except ValueError as err:
            escolha = 0
            print("Formato Errado")
        try:
            n2 = int(input("Subtraendo: "))
        except ValueError as err:
            escolha = 0
            print("Formato Errado")
        if escolha > 0:
            print("{} - {} = {}".format(n1,n2,(n1-n2)))
    elif escolha == 4:
        print("||||||||||||||||||||||||||||||||||||||||||||||||\nDivisão:\n... ")
        try:
            n1 = int(input("Dividendo: "))
        except ValueError as err:
            escolha = 0
            print("Formato Errado")
        try:
            n2 = int(input("Divisor: "))
        except ValueError as err:
            escolha = 0
            print("Formato Errado")
        if escolha > 0:
            print("{} / {} = {}".format(n1,n2,(n1/n2)))
            print("e o resto da divisão é {}".format(n1%n2))
    elif escolha == 5 :
        print("Obrigado, tchau!")
