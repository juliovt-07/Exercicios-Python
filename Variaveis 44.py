degrau = float(input("Insira a altura do degrau (em centímetros): "))
alt = float(input("Insira a sua meta desejada (em metros): "))
converter = degrau/100
print("Para chegar em sua meta, Você precisará subir ",(alt/converter)," Degraus")