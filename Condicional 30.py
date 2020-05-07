#Faça um programa que receba três números e mostre-os em ordem crescente.
n1 = int(input("1º Número: "))
n2 = int(input("2º Número: "))
n3 = int(input("3º Número: "))
if n1 == n2 and n2 == n3:
    print("{}\n{}\n{}".format(n1,n2,n3))
elif n1 > n2 and n1 > n3:
    if n2 > n3:
        print("{}\n{}\n{}".format(n3,n2,n1))
    if n3 > n2:
        print("{}\n{}\n{}".format(n2,n3,n1))
    if n2 == n3:
        print("{}\n{}\n{}".format(n2,n3,n1))
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print("{}\n{}\n{}".format(n3,n1,n2))
    if n3 > n1:
        print("{}\n{}\n{}".format(n1,n3,n2))
    if n1 == n3:
        print("{}\n{}\n{}".format(n1,n3,n2))
elif n3 > n1 and n3 > n2:
    if n1 > n2:
        print("{}\n{}\n{}".format(n2,n1,n3))
    if n2 > n1:
        print("{}\n{}\n{}".format(n1,n2,n3))
    if n2 == n1:
        print("{}\n{}\n{}".format(n1,n2,n3))