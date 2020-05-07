#programa que leia o código do produto escolhido do cardápio de uma
#lanchonete e a quantidade. O programa deve calcular o valor
#a ser pago por aquele lanche. Considere que a cada execução
#somente será calculado um pedido. O cardápio da lanchonete
#segue o padrão abaixo:
cachorro_quente = [100, 1.20]
bauru_simples = [101, 1.30]
bauru_com_ovo = [102, 1.50]
hamburguer = [103, 1.20]
cheeseburguer = [104, 1.70]
suco = [105, 2.20]
refrigerante = [106, 1.00]
escolha = ord("s")
while escolha == 115 or escolha == 83:
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[Código] ------------------------- Valor")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[ {} ] Cachorro Quente ---------- {} R$\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[ {} ] Bauru Simples ------------ {} R$\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[ {} ] Bauru com Ovo ------------ {} R$\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[ {} ] Hamburguer --------------- {} R$\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[ {} ] Cheeseburguer ------------ {} R$\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[ {} ] Suco --------------------- {} R$\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[ {} ] Refrigerante ------------- {} R$\n".format(cachorro_quente[0],cachorro_quente[1],bauru_simples[0],bauru_simples[1],bauru_com_ovo[0],bauru_com_ovo[1],hamburguer[0],hamburguer[1],cheeseburguer[0],cheeseburguer[1],suco[0],suco[1],refrigerante[0],refrigerante[1]))
    codigo = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t----------------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tInforme o código do produto: "))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t----------------------------------------")
    if codigo < 100 or codigo > 106:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCódigo Inválido")
    elif codigo == cachorro_quente[0]:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCachorro Quente")
        valor = cachorro_quente[1]
        quantidade = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tQuantidade: "))
    elif codigo == bauru_simples[0]:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tBauru Simples")
        valor = bauru_simples[1]
        quantidade = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tQuantidade: "))
    elif codigo == bauru_com_ovo[0]:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tBauru com Ovo")
        valor = bauru_com_ovo[1]
        quantidade = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tQuantidade: "))
    elif codigo == hamburguer[0]:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tHamburguer")
        valor = hamburguer[1]
        quantidade = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tQuantidade: "))
    elif codigo == cheeseburguer[0]:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCheeseburguer")
        valor = cheeseburguer[1]
        quantidade = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tQuantidade: "))
    elif codigo == suco[0]:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSuco")
        valor = suco[1]
        quantidade = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tQuantidade: "))
    elif codigo == refrigerante[0]:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tRefrigerante")
        valor = refrigerante[1]
        quantidade = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tQuantidade: "))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tValor: {} R$".format(valor*quantidade))
    escolha = str(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t----------------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[ Tecla ]\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[ s ] ------ Novo Pedido\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[ n ] ------ Sair\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTecla: "))
    escolha = ord(escolha)
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t-----------------------------------------\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAté Mais!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\te\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tObrigado Pela Preferência!")