distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))

if distancia <= 100:
    valor_frete = 1 * peso  
elif 101 <= distancia <= 300:
    valor_frete = 1.50 * peso  
else:
    valor_frete = 2 * peso  

if peso > 10:
    valor_frete += 10


print(f"O valor do frete é: R$ {valor_frete:.2f}")
