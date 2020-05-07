#Escreva um programa que, dado o valor da venda, imprima a
#comissão que deverá ser paga ao vendedor.
#Para calcular a comissão, considere a tabela abaixo:
escolha = ord("r")
w = True
while w == True:
    valor = float(input("Valor da Venda: "))
    com = int
    if valor < 0:
        print("Valor Inválido!")
    elif valor >= 100000:
        com = 700+(valor*0.16)
    elif valor < 100000 and valor >= 80000:
        com = 650+(valor*0.14)
    elif valor < 80000 and valor >= 60000:
        com = 600+(valor*0.14)
    elif valor < 60000 and valor >= 40000:
        com = 550+(valor*0.14)
    elif valor < 40000 and valor >= 20000:
        com = 500+(valor*0.14)
    elif valor < 20000:
        com = 400+(valor*0.14)
    elif valor == 0:
        print("Um Valor maior que 0 por favor")
    print(f"Comissão do vendedor: {com:.2f} R$")
    print("--"*16)
    escolha = str(input("[ s ] Sair\n[ r ] Repetir\n--> "))
    escolha = ord(escolha)
    if escolha == ord("r") or escolha == ord("R"):
        w = True
        print("--"*16)
    else:
        w = False
        print("Acabou, um cheiro e um queijo")