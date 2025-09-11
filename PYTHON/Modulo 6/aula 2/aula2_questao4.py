qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []

print("Digite os", qtd1, "elementos da lista 1:")
for i in range(qtd1):
    valor = int(input())
    lista1.append(valor)

qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []

print("Digite os", qtd2, "elementos da lista 2:")
for i in range(qtd2):
    valor = int(input())
    lista2.append(valor)

intercalada = []

tamanho_menor = min(qtd1, qtd2)
for i in range(tamanho_menor):
    intercalada.append(lista1[i])
    intercalada.append(lista2[i])

if qtd1 > qtd2:
    for i in range(tamanho_menor, qtd1):
        intercalada.append(lista1[i])
        
elif qtd2 > qtd1:
    for i in range(tamanho_menor, qtd2):
        intercalada.append(lista2[i])

print("Lista intercalada:", intercalada)
