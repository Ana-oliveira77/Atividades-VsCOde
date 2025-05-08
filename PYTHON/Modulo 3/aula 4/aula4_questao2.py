nota_filme = int (input("Defina a nota do filme de 1 a 5: "))

if nota_filme == 5: 
  print("Excelente!")
elif nota_filme == 4: 
  print("Muito Bom!")
elif nota_filme == 3: 
  print("Bom!")
elif nota_filme == 2: 
  print("Regular.")
elif nota_filme == 1: 
  print("Ruim.")
else:
  print("Avaliação inválida. Insira um valor entre 1 e 5.")
