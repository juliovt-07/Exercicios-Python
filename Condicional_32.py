cachorro_quente = [100, 1.20]
bauru_simples = [101, 1.30]
bauru_com_ovo = [102, 1.50]
hamburguer = [103, 1.20]
cheeseburguer = [104, 1.70]
suco = [105, 2.20]
refrigerante = [106, 1.00]
escolha = ord("s")
while escolha == 115 or escolha == 83:
    print("\t"*16+"[Código] ------------------------- Valor")
    print("\t"*16+f"[ {cachorro_quente[0]} ] Cachorro Quente ---------- {cachorro_quente[1]} R$\n","\t"*16+f"[ {bauru_simples[0]} ] Bauru Simples ------------ {bauru_simples[1]} R$\n","\t"*16+f"[ {bauru_com_ovo[0]} ] Bauru com Ovo ------------ {bauru_com_ovo[1]} R$\n","\t"*16+f"[ {hamburguer[0]} ] Hamburguer --------------- {hamburguer[1]} R$\n","\t"*16+f"[ {cheeseburguer[0]} ] Cheeseburguer ------------ {cheeseburguer[1]} R$\n","\t"*16+f"[ {suco[0]} ] Suco --------------------- {suco[1]} R$\n","\t"*16+f"[ {refrigerante[0]} ] Refrigerante ------------- {refrigerante[1]} R$\n")
    #print("\t"*16+"--"*20)
    #codigo = int(input("\t"*16+"Informe o codigo:: "))
    try:
        codigo = int(input("\t"*16+"----------------------------------------\n"+"\t"*16+"Informe o código do produto: "))
    except ValueError as err:
        codigo = 0
        valor = 0
        quantidade = 0
    print("\t"*16+"-"*20)
    if codigo < 100 or codigo > 106:
        print("\t"*16+"Código Inválido")
        print("\t"*16+"[ s ] Tentar Novamente")
        print("\t"*16+"[ n ] Cancelar")
        escolha = str(input("\t"*16+"Tecla: "))
    elif codigo == cachorro_quente[0]:
        print("\t"*16+"Cachorro Quente")
        valor = cachorro_quente[1]
        quantidade = int(input("\t"*16+"Quantidade: "))
    elif codigo == bauru_simples[0]:
        print("\t"*16+"Bauru Simples")
        valor = bauru_simples[1]
        quantidade = int(input("\t"*16+"Quantidade: "))
    elif codigo == bauru_com_ovo[0]:
        print("\t"*16+"Bauru com Ovo")
        valor = bauru_com_ovo[1]
        quantidade = int(input("\t"*16+"Quantidade: "))
    elif codigo == hamburguer[0]:
        print("\t"*16+"Hamburguer")
        valor = hamburguer[1]
        quantidade = int(input("\t"*16+"Quantidade: "))
    elif codigo == cheeseburguer[0]:
        print("\t"*16+"Cheeseburguer")
        valor = cheeseburguer[1]
        quantidade = int(input("\t"*16+"Quantidade: "))
    elif codigo == suco[0]:
        print("\t"*16+"Suco")
        valor = suco[1]
        quantidade = int(input("\t"*16+"Quantidade: "))
    elif codigo == refrigerante[0]:
        print("\t"*16+"Refrigerante")
        valor = refrigerante[1]
        quantidade = int(input("\t"*16+"Quantidade: "))
    print("\t"*16+"Valor: {:.2f} R$".format(valor*quantidade))
    escolha = str(input("\t"*16+"----------------------------------------\n"+"\t"*16+"[ Tecla ]\n"+"\t"*16+"[ s ] ------ Novo Pedido\n"+"\t"*16+"[ n ] ------ Sair\n"+"\t"*16+"Tecla: "))
    escolha = escolha[0]
    escolha = ord(escolha)
print("\t"*16+"-----------------------------------------\n"+"\t"*16+"Até Mais!\n"+"\t"*16+"e\n"+"\t"*16+"Obrigado Pela Preferência!")