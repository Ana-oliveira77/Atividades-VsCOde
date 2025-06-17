

while True:
    try:
        cont=0
       
        n = int(input("Digite um número inteiro positivo: "))
        if n > 0:
            break
    except:
        continue

soma = 0
expressao = ""

for i in range(1, n + 1):
    soma += i
    expressao += f"{i}+" if i < n else f"{i}"

print(f"{expressao}")
print(f"A soma dos números de 1 a {n} é {soma}.")








# n1= float(input ("Primeiro número: "))
# n2= float(input ("Segundo número: "))
# n3= float(input ("Terceiro número: "))
# n4= float(input ("Quarto número: "))
# n5= float(input ("Quinto número: "))
# n6= float(input ("Sexto número: "))
# n7= float(input ("Sétimo número: "))
# n8= float(input ("Oitavo número: "))
# n9= float(input ("Nono número: "))
# n10= float(input ("Décimo número: "))

# n=10
# soma= (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10)
# media= soma/n
# print (f"A média dos números digitados é:  {media:.2f}")
