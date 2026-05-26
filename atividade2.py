# Calculadora simples feita em python,
# By mark

#Variaveis
soma = int
subtraçao = int
multiplicaçao = int
divisao = int
resultado = 0
# Perguntas
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

pergunta = input("Qual a operação que deseja realizar? (soma, subtração, multiplicação ou divisão): ").lower()
# Condicionais
if pergunta == "soma":
    resultado = numero1 + numero2
    print("O resultado da soma é: ", resultado)

elif pergunta == "subtração":
     resultado = numero1 - numero2
     print("O resultado da subtração é: ", resultado)

elif pergunta == "multiplicaçao":
      resultado = numero1 * numero2
      print("O resultado da multiplicação é: ", resultado)

elif pergunta == "divisao":
    resultado = numero1 / numero2
    print("O resultado da divisão é: ", resultado)
else:
    print("invalido")
