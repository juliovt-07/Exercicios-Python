#Escreva o menu de opções abaixo. Leia a opção do usuário
#e execute a operação escolhida. Escreva uma mensagem de erro
#se a opção for inválida.
#Escolha a opção:
#1- Soma de 2 números.
#2- Diferença entre 2 números (maior pelo menor).
#3- Produto entre 2 números.
#4- Divisão entre 2 números (o denominador nao pode ser zero). Opção
escolha = 1
while escolha < 5 or escolha >= 6:
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("'1' Soma de 2 números: ")
    print("'2' Diferença entre 2 números(Maior pelo menor): ")
    print("'3' Produto entre 2 números: ")
    print("'4' Divisão entre 2 números: ")
    try:
        escolha = int(input("Escolha uma opção de 1 a 4 ('5' para Sair): "))
    except ValueError as err:
        print('Formato Errado')
        escolha = 0
    if escolha <= 0 or escolha > 5:
        print("Opção Inválida!")
    elif escolha == 1:
        print("||||||||||||||||||||||||||||||||||||||||||||||||\nSoma de 2 números:\n... ")
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
        print("||||||||||||||||||||||||||||||||||||||||||||||||\nDiferença entre 2 números:\n... ")
        try:
            n1 = int(input("Primeiro número: "))
        except ValueError as err:
            escolha = 0
            print("Formato Errado")
        try:
            n2 = int(input("Segundo número: "))
        except ValueError as err:
            escolha = 0
            print("Formato errado")
        if escolha >= 0:
            if n1 > n2:
                print("A Diferença entre {} e {} é: {}".format(n1,n2,(n1-n2)))
            if n2 > n1:
                print("A Diferença entre {} e {} é: {}".format(n2,n1,(n2-n1)))
            if n1 == n2:
                print("Ambos tem o mesmo valor!")
    elif escolha == 3:
        print("||||||||||||||||||||||||||||||||||||||||||||||||\nProduto entre 2 números:\n")
        try:
            n1 = int(input("Primeiro número: "))
        except ValueError as err:
            escolha = 0
            print("Formato Errado")
        try:
            n2 = int(input("Segundo número: "))
        except ValueError as err:
            escolha = 0
            print("Formato Errado")
        if escolha > 0:
            print("Produto: {}".format((n1*n2)))
    elif escolha == 4:
        print("||||||||||||||||||||||||||||||||||||||||||||||||\nDivisão entre 2 números:\n... ")
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