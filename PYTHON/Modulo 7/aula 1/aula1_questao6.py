from itertools import permutations

frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

palavras = frase.split()
anagramas = [''.join(p) for p in permutations(objetivo)]

resultado = [palavra for palavra in palavras if palavra in anagramas]
print("Anagramas:", resultado)
