number1 = int(input("Digite o 1º número: "))
operation = input("Qual operação você deseja? [+, -, /, X]: ")
number2 = int(input("Digite o 2º número: "))

if operation == "+":
    resultsoma = number1 + number2
    print(f"Resultado da soma: {resultsoma}")
elif operation == "-":
    resultsub = number1 - number2
    print(f"Resultado da subtração: {resultsub}")
elif operation == "*":
    resultmult = number1 * number2
    print(f"Resultado da multiplicação: {resultmult}")
else:
    resultdiv = number1 / number2
    print(f"Resultado da divisão: {resultdiv}")
