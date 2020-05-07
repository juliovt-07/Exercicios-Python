carro = float(input("Valor do Carro: "))
distribuidor = 0
imposto = 0
valorTotal = 0
if carro < 0:
    print("Valor Inválido!")
elif carro > 0 and carro <= 12000:
    distribuidor = carro*0.05
    imposto = 0
    valorTotal = carro+distribuidor+imposto
    #print(f"{distribuidor}\n{imposto}")
    print(f"Custo Total: {valorTotal} R$")
elif carro > 12000 and carro <= 25000:
    distribuidor = carro*0.10
    imposto = carro*0.15
    valorTotal = carro+distribuidor+imposto
    #print(f"{distribuidor}\n{imposto}")
    print(f"Custo Total: {valorTotal} R$")
elif carro > 25000:
    distribuidor = carro*0.15
    imposto = carro*0.20
    valorTotal = carro+distribuidor+imposto
    #print(f"{distribuidor}\n{imposto}")
    print(f"Custo Total: {valorTotal} R$")
