def pares_unicos(numeros, soma_objetivo):
    pares = set()
    vistos = set()
    for num in numeros:
        complemento = soma_objetivo - num
        if complemento in vistos:
            pares.add(tuple(sorted((num, complemento))))
        vistos.add(num)
    return list(pares)

nums = [3, 4, 5, 6, 7]
soma = 10
resultado = pares_unicos(nums, soma)
print(resultado)
