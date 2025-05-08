num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

resto = num1 + num2
resto = resto % 2

if resto == 0:
  print("Par")
else:
  print ("Ímpar")

