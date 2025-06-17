from collections import Counter

lista1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lista2 = [1, 1, 2, 4, 5, 6]

cont1 = Counter(lista1)
cont2 = Counter(lista2)

diferenca = list((cont1 - cont2).elements())
print(diferenca)
