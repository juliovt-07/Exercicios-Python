altura = float(input("Altura: "))
peso = float(input("Peso: "))
altura = altura*altura
imc = peso/altura
print(f"IMC: {imc:.2f}")
if imc < 0:
    print("IMC Inválido")
elif imc > 0 and imc < 18.5:
    print("Abaixo do Peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Saudável")
elif imc >= 25 and imc <= 29.5:
    print("Peso em excesso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade Grau I")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade Grau II (severa)")
elif imc >= 40:
    print("Obesidade Grau III (mórbida)")