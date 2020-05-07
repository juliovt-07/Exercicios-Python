#programa que receba dois números e mostre qual deles é o maior.
n1 = int(input("n1 "))
n2 = int(input("n2 "))

if n1 > n2 :
    print(n1," é maior que ",n2)
if n2 > n1 :
    print(n2," é maior que ",n1)
if n1 == n2 :
    print("Ambos tem o mesmo valor")