genero = input("Digite seu genero (M ou F): ")
idade = int(input("Digite sua idade: "))
tempo_servico = int (input("Digite seu tempo de serviços em anos: "))

a = (genero == 'f' and idade >= 60) or \
    (genero == 'm' and idade >= 65)
b = tempo_servico >= 30
c = idade >= 60 and tempo_servico >= 25

apto = a or b or c

print(apto)