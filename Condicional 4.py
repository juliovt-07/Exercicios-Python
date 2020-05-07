#programa que leia um número e,
#caso ele seja positivo, calcule e mostre:
#• O número digitado ao quadrado
#• A raiz quadrada do número digitado
n = int(input("Digite um número: "))
if n%2 == 0:
    print(f"{n} É Positivo")
else:
    print(f"{n} É Negativo")