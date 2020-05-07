#Uma empresa vende o mesmo produto para quatro diferentes estados.
#Cada estado possui uma taxa diferente de imposto sobre o produto
#(MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa
#em que o usuário entre com o valor e o estado destino do produto
#e o programa retorne o preço final
#do produto acrescido do imposto do estado em que ele será vendido.
#Se o estado digitado não for válido, mostrar uma mensagem de erro.
valor = float(input("Valor do produto: "))
print("Escolha o Estado Destino dentre estes:")
print("[Mg] - Minas Gerais")
print("[Sp] - São Paulo")
print("[Rj] - Rio de Janeiro")
print("[Ms] - Mato Grosso do Sul")
estado = str(input("Estado: "))
mg, Mg, MG = [109, 103],[77, 103],[77, 71]
sp, Sp, SP = [115, 112],[83, 112],[83, 80]
rj, Rj, RJ = [114, 106],[82, 106],[82, 74]
ms, Ms, MS = [109, 115], [77, 115],[77, 83]
estado = [ord(estado[0]),ord(estado[1])]
if valor <= 0:
    print("Valor Inválido")
elif estado == mg or estado == Mg or estado == MG:
    print("Valor do Produto + Taxa de imposto do Estado:\n{}".format(valor+(valor*0.07)))
elif estado == sp or estado == Sp or estado == SP:
    print("Valor do Produto + Taxa de imposto do Estado:\n{}".format(valor+(valor*0.12)))
elif estado == rj or estado == Rj or estado == RJ:
    print("Valor do Produto + Taxa de imposto do Estado:\n{}".format(valor+(valor*0.15)))
elif estado == ms or estado == Ms or estado == MS:
    print("Valor do Produto + Taxa de imposto do Estado:\n{}".format(valor+(valor*0.08)))
else:
    print("Esse Estado não está incluso na Lista!")