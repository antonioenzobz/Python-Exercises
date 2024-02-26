print ("------Qual operação deseja fazer?------")
print ("1 - Adição")
print ("2 - Subtração")
print ("3 - Multiplicação")
print ("4 - Divisão")
print ("--------------------------------------")

#Variáveis
op = int(input("Digite o número corresponde ao tipo de operação que deseja fazer: "))
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

#Realizando a operação
if op == 1:
  print ("Seu resultado é:", float(n1 + n2))
elif op == 2:
  print ("Seu resultado é:", float(n1 - n2))
elif op == 3:
  print ("Seu resultado é:", float(n1 * n2))
elif op == 4:
  print ("Seu resultado é:", float(n1 / n2))
else:
  print ("Entrada inválida!")
  