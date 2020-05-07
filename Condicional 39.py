repetir = ord("s")
escolha = ord("s")
while repetir == 115 or repetir == 83:
    salario = float(input("Salario Atual: "))
    tempo = int(input("Anos de Serviço: "))
    if salario > 2000 and tempo == 0:
        print("[ Sem direito a reajuste de salário ]")
        escolha = ord("n")
    else:
        if salario < 0:
            print("Salário Inválido")
            escolha = ord("n")
        elif salario > 0 and salario <= 500:
            salario = salario+(salario*0.25)
            escolha = ord("n")
        elif salario > 500 and salario <= 1000:
            salario = salario+(salario*0.20)
            escolha = ord("n")
        elif salario > 1000 and salario <= 1500:
            salario = salario+(salario*0.15)
            escolha = ord("n")
        elif salario > 1500 and salario <= 2000:
            salario = salario+(salario*0.10)
            escolha = ord("n")
        elif salario > 2000:
            salario = salario
        escolha = ord("n")
    escolha = ord("s")
    while escolha == 115:
        if tempo < 0:
            print("Tempo Inválido")
        elif tempo == 0:
            salario = salario
        elif tempo >= 1 and tempo <= 3:
            salario = salario+100
        elif tempo >= 4 and tempo <= 6:
            salario = salario+200
        elif tempo >= 7 and tempo <= 10:
            salario = salario+300
        elif tempo > 10:
            salario = salario+500
        escolha = ord("n")
    print(f"Reajuste: {salario} R$")
    repetir = str(input("Repetir? (s / n): "))
    repetir = ord(repetir)
    print("--"*10)
print("Obrigado, um cheiro e um queijo")