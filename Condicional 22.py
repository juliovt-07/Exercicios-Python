#Leia a idade e o tempo de serviço de um trabalhador e
#escreva se ele pode ou não se aposentar.
#As condições para aposentadoria são
#• Ter pelo menos 65 anos,
#• Ou ter trabalhado pelo menos 30 anos,
#• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
idade = int(input("Idade: "))
tempo = int(input("Tempo de Serviço: "))
ap = bool(False)
if idade >= 65:
    ap = True
if tempo >= 30:
    ap = True
if idade >= 60 and tempo >= 25:
    ap = True
if tempo >= idade:
    print("Quer Dizer que você tem {} anos e já trabalhou por {}?\nAcho que você está mentindo hein!\nMENTIROSO".format(idade,tempo))
    ap = False
if ap == True:
    print("Aposentadoria Aprovada!")
else:
    print("Aposentadoria Não-Aprovada!")