#numero real. Se o número for positivo imprima a raiz quadrada.
#Do contrário, imprima o numero ao quadrado.
n = float(input("Insira um valor: "))
d = 2
if n >= 0:
    #positivo
    print(f"Raíz quadrada: {n**0.5:.1f}")
else:
    #negativo
    print(f"Ao quadrado: {n*n}")