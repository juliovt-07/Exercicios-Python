#programa que calcule e mostre a área de um trapézio. Sabe-se que:
#A = (basemaior + basemenor) ∗ altura / 2
#Lembre-se a base maior e a base menor devem ser números maiores que zero.
altura = float(input("Altura do trapézio: "))
basemaior = float(input("Base maior: "))
basemenor = float(input("Base menor: "))
if basemenor <= 0 or basemaior <= 0:
    print("Os valores das base devem ser maiores de '0'")
else:
    print("Área do trapézio: ",(((basemaior+basemenor)*altura)/2))
