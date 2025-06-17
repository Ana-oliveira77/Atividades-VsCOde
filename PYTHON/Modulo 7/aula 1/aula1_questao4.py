numero = input("Digite o número: ")

numero_limpo = numero.replace("-", "").replace(" ", "")

if len(numero_limpo) < 8:
    print("Número inválido. Digite pelo menos 8 dígitos.")
else:
    digitos_finais = numero_limpo[-8:]
    resultado = "+55 31 " + digitos_finais
    print("Número com DDD:", resultado)
