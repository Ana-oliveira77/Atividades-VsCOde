personagem = input("Escolha a classe do seu personagem (guerreiro, mago, arqueiro): ")
ponto_str = int(input("Digite os pontos de força (de 1 a 20):"))
ponto_int = int(input("Digite os pontos de magia (de 1 a 20):"))


apto = ((personagem == 'guerreiro') and (ponto_str >=15 and ponto_int<=10)) or ((personagem == 'mago') and (ponto_str <=10 and ponto_int>=15)) or ((personagem == 'arqueiro') and ((ponto_str >=5 and ponto_int>=5) and (ponto_int <=15 and ponto_str <=15)))

print(apto)