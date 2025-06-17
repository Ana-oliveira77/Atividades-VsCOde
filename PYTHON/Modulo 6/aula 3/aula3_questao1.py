entrada = input("Digite pelo menos 4 números inteiros separados por espaço: ")
lista = list(map(int, entrada.split()))

if len(lista) < 4:
    print("Você precisa digitar pelo menos 4 números.")
else:
    print("Lista original:", lista)
    print("3 primeiros elementos:", lista[:3])
    print("2 últimos elementos:", lista[-2:])
    print("Lista invertida:", lista[::-1])
    print("Elementos de índice par:", lista[::2])
    print("Elementos de índice ímpar:", lista[1::2])
