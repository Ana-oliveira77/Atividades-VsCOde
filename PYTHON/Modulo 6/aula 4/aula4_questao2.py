frase = input("Digite uma frase: ").lower()

vogais = sorted([letra for letra in frase if letra in "aeiou"])
consoantes = [letra for letra in frase if letra.isalpha() and letra not in "aeiou"]

print("Vogais:", vogais)
print("Consoantes:", consoantes)
