inserção = False

while inserção == False:
  try:
    numero1 = float (input("Número 1: ")) 
    inserção == True
    break
  except ValueError:
    print("Caractere inválido, favor digitar um número")

operacao = input("Operação (+, -, *, /, $)")

if operacao == "$":
  resultado = (numero1 ** (1 / 2))
 
  convert = str(resultado).split(".")[1]

  terceiracasa = convert[2]

  if float(terceiracasa) > 5:
    print("O resultado é", "{:.3f}".format(resultado))
  else:
    print("O resultado é", "{:.2f}".format(resultado))
        
else:
  numero2 = float(input("Número 2: "))

if operacao == "+":
  resultado = (numero1 + numero2)
  print (resultado)
elif operacao == "-":
  resultado = (numero1 - numero2)
  print (resultado)
elif operacao == "*":
  resultado = (numero1 * numero2)
  print (resultado)
elif operacao == "/":
  resultado = (numero1 / numero2)
  print (resultado)