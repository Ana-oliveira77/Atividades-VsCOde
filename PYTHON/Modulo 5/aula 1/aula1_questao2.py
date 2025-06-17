import random
import math

n = int(input("Quantos números aleatórios você quer gerar? "))

soma = 0

for _ in range(n):
    numero = random.randint(0, 100)
    soma += numero

raiz = math.sqrt(soma)

print(f"A raiz quadrada da soma dos {n} números é: {raiz}")
