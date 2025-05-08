prod1_nome = input("Digite o nome do produto 1 ")
prod1_preco = float(input("Digite o valor do produto 1 "))
prod1_qtd = int(input("Digite a quantidade do produto 1 "))
prod2_nome = input("Digite o nome do produto 2 ")
prod2_preco = float(input("Digite o valor do produto 2 "))
prod2_qtd = int(input("Digite a quantidade do produto 2 "))
prod3_nome = input("Digite o nome do produto 3 ")
prod3_preco = float(input("Digite o valor do produto 3 "))
prod3_qtd = int(input("Digite a quantidade do produto 3 "))

total = (prod1_preco*prod1_qtd) + (prod2_preco*prod2_qtd)+(prod3_preco*prod3_qtd)

print (f"Total: R$ {total:,.2f}")