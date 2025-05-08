n= int(input(" Quantos participantes? "))
soma= 0
cont= 0   

while cont< n:
 idade= int(input(" Qual a idade do participante? "))
 soma += idade

 cont += 1   

print (soma)
print (("A média das idades é:" )(soma/n))