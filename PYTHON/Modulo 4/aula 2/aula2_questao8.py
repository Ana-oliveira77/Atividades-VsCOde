resultado = 0
operador = "+"
primeiro_numero = True

while True:
    entrada = input()

    if entrada == "Fim":
        break

    if primeiro_numero:
        resultado = int(entrada)
        primeiro_numero = False
        continue

    if entrada == "+" or entrada == "-":
        operador = entrada
        continue

    numero = int(entrada)
    if operador == "+":
        resultado += numero
    elif operador == "-":
        resultado -= numero

print(resultado)
