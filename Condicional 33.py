#Um produto vai sofrer aumento de acordo com a tabela abaixo.
#Leia o preço antigo, calcule e escreva o preço novo, e escreva
#uma mensagem em função do preço novo (de acordo com a segunda tabela).
preco = [float(input("Preço Antigo: ")),0]
if preco[0] < 0:
    print("Preço Inválido!")
elif preco[0] > 0 and preco[0] <= 50:
    preco[1] = preco[0]+(preco[0]*0.05)
elif preco[0] > 50 and preco[0] <= 100:
    preco[1] = preco[0]+(preco[0]*0.10)
elif preco[0] > 100:
    preco[1] = preco[0]+(preco[0]*0.15)
print("Novo Preço: {} R$".format(preco[1]))