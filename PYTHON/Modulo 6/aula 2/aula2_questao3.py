import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

intersecao = sorted(set(lista1) & set(lista2))

contagem = {}
for valor in intersecao:
    contagem[valor] = (lista1.count(valor), lista2.count(valor))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção (sem duplicatas):", intersecao)
print("Contagem:")
for valor, (c1, c2) in contagem.items():
    print(f"{valor}: (lista1 = {c1}, lista2 = {c2})")
