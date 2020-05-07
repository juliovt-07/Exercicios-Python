#programa que leia um número inteiro maior do que zero e devolva,
#na tela, a soma de todos os seus algarismos. Por exemplo,
#ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o
#número lido não for maior do que zero,
#o programa terminará com a mensagem “Número inválido”.
n1 = float(input("Número da desgrama "))
s1 = (int(n1/100))
s2 = (int((n1%100)/10))
s3 = (int((n1%100)%10))

if n1 >= 0 :
    print(s1,"+",s2,"+",s3,"=",s1+s2+s3)
else :
    print("Número Inválido")