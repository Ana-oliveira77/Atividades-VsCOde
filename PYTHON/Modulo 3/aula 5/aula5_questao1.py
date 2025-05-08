print (" Calculadora, digite a operação a ser feita")
num1= float(input () )
operacao= input ()
num2= float(input () )

if operacao=="+":
   resultado= num1+num2
elif operacao== "-":
   resultado= num1-num2
elif operacao== "*":
   resultado= num1*num2
elif operacao== "/":
   resultado= num1/num2
else:
   print("Operação inválida") 

print (("Seu resultado é: ")+ f"{num1} {operacao} {num2} = {resultado}")



