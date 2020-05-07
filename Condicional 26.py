#Leia a distância em Km e a quantidade de litros de gasolina consumidos
#por um carro em um percurso, calcule o consumo em Km/l e
#escreva uma mensagem de acordo com a tabela abaixo:
km = float(input("Distância percorrida (Km): "))
l = float(input("Gasolina consumida (L): "))
calc = int(km/l)
if km < 0:
    print("Valor Inválido")
elif calc < 8:
    print("Venda o carro")
elif calc >= 8 and calc <= 14:
    print("Econômico")
elif calc > 14:
    print("Super Econômico")