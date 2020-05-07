idade = int(input("Idade: "))
c = "Categoria:\n"
if idade < 5:
    print("Idade Inválida")
elif idade >= 5 and idade <= 7:
    print(c+"Infantil A")
elif idade >= 8 and idade <= 10:
    print(c+"Infantil B")
elif idade >= 11 and idade <= 13:
    print(c+"Juvenil A")
elif idade >= 14 and idade <= 17:
    print(c+"Juvenil B")
elif idade >= 18:
    print(c+"Sênior")