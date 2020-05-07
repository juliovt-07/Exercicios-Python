#número fornecido pelo usuário.
#Se esse número for positivo, calcule a raiz quadrada do
#número. Se o número for negativo,
#mostre uma mensagem dizendo que o número é inválido.
n1 = int(input("número: "))
if n1 >= 0 :
    #Cáculo errado
    print("A Raíz quadrada é {:.1f}".format(n1**0.5))
else :
    print("Número Inválido")