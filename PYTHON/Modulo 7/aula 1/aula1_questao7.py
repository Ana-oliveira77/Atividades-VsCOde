import random

def encrypt(lista_strings):
    chave = random.randint(1, 10)
    resultado = []

    for palavra in lista_strings:
        nova = ""
        for letra in palavra:
            nova += chr((ord(letra) + chave - 32) % 95 + 32)
        resultado.append(nova)

    return resultado, chave

nomes = ["banana", "uva", "maca", "manga", "pera", "limao"]
criptografado, chave = encrypt(nomes)
print("Chave:", chave)
print("Nomes criptografados:", criptografado)
