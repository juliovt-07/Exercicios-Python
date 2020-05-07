#Dados três valores, A, B, C, verificar se eles podem ser valores
#dos lados de um triângulo e, se forem, se é um triângulo escaleno,
#equilátero ou isóscele, considerando os seguintes conceitos:
#• O comprimento de cada lado de um triângulo é menor do que
#a soma dos outros dois lados.
#• Chama-se equilátero o triângulo que tem três lados iguais.
#• Denominam-se isósceles o triângulo que tem
#o comprimento de dois lados iguais.
#•Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
print("Insira os valores")
ta, tb, tc = bool, bool, bool
A = float(input("Valor 'A': "))
B = float(input("Valor 'B': "))
C = float(input("Valor 'C': "))
if A <= (B+C):
    ta = True
else:    ta = False
if B <= (A+C):
    tb = True
else:    tb = False
if C <= (A+B):
    tc = True
else:    tc = False
if ta == True & tb == True & tc == True:
    print("É um Triângulo:")
if A == B and A == C:
    print("Equilátero")
if A == (B+C) or B == (A+C) or C == (A+B):
    print("Isósceles")
if A != B and A != C and B != C:
    print("Escaleno")
