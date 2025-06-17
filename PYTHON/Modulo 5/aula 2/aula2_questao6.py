par_ou_impar = lambda x: "par" if x % 2 == 0 else "ímpar"

print("Digite os valores (0 para sair):")
while True:
    num = int(input())
    if num == 0:
        break
    print(par_ou_impar(num))
