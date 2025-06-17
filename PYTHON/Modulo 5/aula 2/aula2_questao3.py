def soma_digitos(n):
    soma = 0
    while n > 0:
        soma += n % 10
        n //= 10
    return soma

n = int(input("Digite um número inteiro: "))
print("A soma dos dígitos é:", soma_digitos(n))
