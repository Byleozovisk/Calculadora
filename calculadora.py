numero1 = (input("Número 1: "))

while not isinstance(numero1, float) and numero1 != "":
  print("Caracter inválido, favor digitar um número")
  numero1 = float(input("Número 1: "))
  
operacao = input("Operação (+, -, *, /, $)")

if operacao == "$":
  resultado = (numero1 ** (1 / 2))
  print(resultado)

  convert = str(resultado).split(".")[1]

  terceiracasa = convert[2]

  print (terceiracasa)

  if float(terceiracasa) > 5:
    print("O resultado é", "{:.3f}".format(resultado))
  else:
    print("O resultado é", "{:.2f}".format(resultado))
        
else:
  numero2 = float(input("Número 2: "))

if operacao == "+":
  resultado = (numero1 + numero2)
elif operacao == "-":
  resultado = (numero1 - numero2)
elif operacao == "*":
  resultado = (numero1 * numero2)
elif operacao == "/":
  resultado = (numero1 / numero2)

print(resultado)

