valorTotal = float(input("Valor Total: "))
dec = valorTotal*0.10
parcela3 = valorTotal/3
coVista = ((valorTotal+dec)*0.5)
coParcelo = valorTotal*0.05
print("Valor Total com 10% de desconto: R$",dec,"\n"
    "Em 3x de R$",parcela3," Sem Juros\n"
    ,"Comissão do vendedor (à Vista): R$",coVista,"\n","Comissão do vendedor (Parcelado): R$",coParcelo))