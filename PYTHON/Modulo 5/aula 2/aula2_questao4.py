def inverteValor(n):
    inverso = 0
    while n > 0:
        inverso = inverso * 10 + n % 10
        n //= 10
    return inverso

def verificaInverso(original, invertido):
    return (original % 2) == (invertido % 2)


valor = int(input("Digite um número: "))
inv = inverteValor(valor)
print("Valor invertido:", inv)
print("Mesma paridade?", verificaInverso(valor, inv))
