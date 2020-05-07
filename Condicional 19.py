#programa para verificar se um determinado número inteiro e divisível
#por 3 ou 5, mas não simultaneamente pelos dois.
n = int(input("Insira um valor inteiro: "))
if n%3 == 0:
    print("{} É divisível por 3".format(n))
else:
    print("{} Não é divisível por 3".format(n))
if n%5 == 0:
    print("{} É divisível por 5".format(n))
else:
    print("{} Não é divisível por 5".format(n))