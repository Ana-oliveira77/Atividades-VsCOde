usuario1= [139, 155, 226]
usuario2= [192, 185, 326]
usuario3= [112, 178, 286]
usuario4= [103, 165, 250]

margem= 5

valordairis1 = int(input ("Digite o primeiro valor de identificação da íris "))
valordairis2 = int(input ("Digite o segundo valor de identificação da íris "))
valordairis3 = int(input ("Digite o terceiro valor de identificação da íris "))

if float(valordairis1 - usuario1[0]) <= margem and float(valordairis2 - usuario1[1]) <= margem and float(valordairis3 - usuario1[2]) <= margem:
    print("Usuário autenticado com sucesso! (Usuario 1)")
elif float(valordairis1 - usuario2[0]) <= margem and float(valordairis2 - usuario2[1]) <= margem and float(valordairis3 - usuario2[2]) <= margem:
    print("Usuário autenticado com sucesso! (Usuario 2)")
elif float(valordairis1 - usuario3[0]) <= margem and float(valordairis2 - usuario3[1]) <= margem and float(valordairis3 - usuario3[2]) <= margem:
    print("Usuário autenticado com sucesso! (Usuario 3)")
elif float(valordairis1 - usuario4[0]) <= margem and float(valordairis2 - usuario4[1]) <= margem and float(valordairis3 - usuario4[2]) <= margem:
    print("Usuário autenticado com sucesso! (Usuario 4)")
else:
    print("Autenticação falhou. Padrão de íris não reconhecido.")