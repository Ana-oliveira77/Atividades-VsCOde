#input para o valor do comprimento
comprimento = int(input("Digite o valor do comprimento "))

#input para o valor da largura
largura = int(input("Digite o valor do Largura "))

#input para o valor do preço
preco = float(input("Digite o valor do preco "))

#formula para calcular area²
area_m2 = comprimento * largura

#formula para calcular o preço da area²
preco_total = preco * area_m2

#print do resultado
print (f"O terreno possui {area_m2}m2 e custa R$ {preco_total:,.2f}")