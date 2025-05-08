n = int (input( "Quantos experimentos foram feitos? "))
cont=0
soma_sapo, soma_rato, soma_coelho= 0,0,0


while cont<n:
    quantia = int(input ("Quantos animais foram utilizados? "))
    tipo= input(("Qual o tipo de animal utilizado? "))

    if tipo == "S":
       soma_sapo += quantia
    elif tipo == "R":
       soma_rato += quantia
    elif tipo == "C":
       soma_coelho += quantia
    else:
       print ("Não identificado")