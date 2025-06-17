produto = 1
valores = []

while True:
    valor = int(input())

    if valor == 0:
        break

    valores.append(valor)

for i in valores:
    if i <= 0:
        continue
    produto *= i

print("Produto:", produto)
