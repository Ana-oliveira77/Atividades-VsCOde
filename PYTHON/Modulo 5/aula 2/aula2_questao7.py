op = input("Opções: (1) maior ou (2) menor?\nOpção: ")

if op == "1":
    func = lambda a, b: a if a > b else b
    msg = "O maior valor é:"
elif op == "2":
    func = lambda a, b: a if a < b else b
    msg = "O menor valor é:"
else:
    print("Opção inválida.")
    exit()

print("\nDigite os valores (0 para finalizar):")
valor = int(input())
if valor == 0:
    print("Nenhum valor inserido.")
else:
    resultado = valor
    while True:
        valor = int(input())
        if valor == 0:
            break
        resultado = func(resultado, valor)

    print(msg, resultado)
