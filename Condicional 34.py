#Leia a nota e o número de faltas de um aluno, e escreva seu conceito.
#De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas
#ocorre uma redução de conceito.
nota = float(input("Nota do aluno: "))
faltas = int(input("Faltas do aluno: "))
if nota < 0:
    print("Nota Inválida!")
elif nota >= 9 and nota <= 10:
    if faltas < 0:
        print("Valor Inválido!")
    elif faltas > 0 and faltas <= 20:
        print("A")
    elif faltas > 20:
        print("B")
elif nota >= 7.5 and nota <= 8.9:
    if faltas < 0:
        print("Valor Inválido!")
    elif faltas > 0 and faltas <= 20:
        print("B")
    elif faltas > 20:
        print("C")
elif nota >= 5 and nota <= 7.4:
    if faltas < 0:
        print("Valor Inválido!")
    elif faltas > 0 and faltas <= 20:
        print("C")
    elif faltas > 20:
        print("D")
elif nota >= 4 and nota <= 4.9:
    if faltas < 0:
        print("Valor Inválido!")
    elif faltas > 0 and faltas <= 20:
        print("D")
    elif faltas > 20:
        print("E")
elif nota >= 0 and nota <= 3.9:
    if faltas < 0:
        print("Valor Inválido!")
    elif faltas > 0 and faltas <= 20:
        print("E")
    elif faltas > 20:
        print("Morreu")