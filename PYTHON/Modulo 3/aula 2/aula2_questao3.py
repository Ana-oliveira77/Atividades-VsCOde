idade = int(input("Digite sua idade: "))
qtd_jogos = str(input("Já jogou pelo menos 3 jogos de tabuleiro?: "))
vencidos = int(input("Quantos jogos já venceu: "))

apto = (idade >=16 and idade <=18) and (qtd_jogos == 'True') and (vencidos >=1)



print(apto)
