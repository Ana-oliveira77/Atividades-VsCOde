import math

def calcula_perimetro_triangulo(l1, l2, l3):
    return l1 + l2 + l3

def calcula_perimetro_circulo(raio):
    return 2 * math.pi * raio

def calcula_perimetro_retangulo(lado1, lado2=0):
    if lado2 == 0:
        return 4 * lado1  
    else:
        return 2 * (lado1 + lado2) 
while True:
    print("\n1 - Calcular perímetro triângulo")
    print("2 - Calcular perímetro círculo")
    print("3 - Calcular perímetro retângulo")
    print("4 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        l1 = int(input("Digite o lado 1: "))
        l2 = int(input("Digite o lado 2: "))
        l3 = int(input("Digite o lado 3: "))
        print("O perímetro é:", calcula_perimetro_triangulo(l1, l2, l3))
    elif opcao == 2:
        raio = int(input("Digite o raio do círculo: "))
        print("O perímetro é:", calcula_perimetro_circulo(raio))
    elif opcao == 3:
        l1 = int(input("Digite o primeiro lado: "))
        l2 = int(input("Digite o segundo lado (0 para quadrado): "))
        print("O perímetro é:", calcula_perimetro_retangulo(l1, l2))
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
