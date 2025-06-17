import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

maior_qtd_negativos = 0
indice_inicio = 0

for i in range(len(lista) - 4):  
    sublista = lista[i:i+5]
    qtd_negativos = len([n for n in sublista if n < 0])
    
    if qtd_negativos > maior_qtd_negativos:
        maior_qtd_negativos = qtd_negativos
        indice_inicio = i

del lista[indice_inicio:indice_inicio+5]

print("Editada:", lista)
