total = float(input("Qual o valor total da compra? R$ "))

if total < 50:
    print("Sem descontos!")
    print(f"Valor total: R$ {total:.2f}")
elif total >= 50 and total < 100:
    desconto = total * 0.10
    resultado = total - desconto
    print("Desconto de 10% atribuído")
    print(f"Valor total com desconto: R$ {resultado:.2f}")
elif total >= 100:
    desconto = total * 0.20
    resultado = total - desconto
    print("Desconto de 20% atribuído")
    print(f"Valor total com desconto: R$ {resultado:.2f}")
