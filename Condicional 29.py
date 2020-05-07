#Faça uma prova de matemática para crianças que estão aprendendo
#a somar números inteiros menores do que 100. Escolha números
#aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a
#soma de a + b, onde a e b são os números aleatórios.
#Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele
#as perguntas e as respostas corretas, além de quantas vezes
#o aluno acertou.
import random
s = int(115)
S = int(83)
n = int(110)
N = int(78)
escolha = str(input("Press Enter ! "))
escolha = int(115)
perguntas = 0
certo = 0
errado = 0
gambiraA = [0,1,2,3,4]
gambiraB = [0,1,2,3,4]
while escolha == s or escolha == S:
    while perguntas < 5:
        a = random.randint(1,100)
        b = random.randint(1,100)
        try:
            resultado = int(input("Qual a soma de {} + {} ? ".format(a,b)))
        except ValueError as err:
            print("Valor inválido !")
            perguntas = 5
        if resultado == (a+b):
            certo = certo+1
        else:
            errado = errado+1
        if perguntas < 0:
            gambiraA[0] = 0
            gambiraB[0] = 0
        elif perguntas == 0:
            gambiraA[0] = a
            gambiraB[0] = b
        elif perguntas == 1:
            gambiraA[1] = a
            gambiraB[1] = b
        elif perguntas == 2:
            gambiraA[2] = a
            gambiraB[2] = b
        elif perguntas == 3:
            gambiraA[3] = a
            gambiraB[3] = b
        elif perguntas == 4:
            gambiraA[4] = a
            gambiraB[4] = b
        perguntas = perguntas+1
    print("{} + {} = {}".format(gambiraA[0],gambiraB[0],(gambiraA[0]+gambiraB[0])))
    print("{} + {} = {}".format(gambiraA[1],gambiraB[1],(gambiraA[1]+gambiraB[1])))
    print("{} + {} = {}".format(gambiraA[2],gambiraB[2],(gambiraA[2]+gambiraB[2])))
    print("{} + {} = {}".format(gambiraA[3],gambiraB[3],(gambiraA[3]+gambiraB[3])))
    print("{} + {} = {}".format(gambiraA[4],gambiraB[4],(gambiraA[4]+gambiraB[4])))
    print("{} erros\n{} acertos".format(errado,certo))
    try:
        escolha = str(input("Repetir? S / N : "))
    except ValueError as err:
        escolha = n
    perguntas = 0
    certo, errado = 0,0
    escolha = ord(escolha)
print("Fim, Tchau, Um cheiro e um Queijo! ")
