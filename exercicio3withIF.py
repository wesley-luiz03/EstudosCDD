number1 = int(input("Digite o 1º número: "))
number2 = int(input("Digite o 2º número: "))
number3 = int(input("Digite o 3º número: "))

if number1 > number2 and number1 > number3:
    print(f"{number1} é o maior número!")  
elif number2 > number1 and number2 > number3:
    print(f"{number2} é o maior número!")
elif number3 > number1 and number3 > number2:
    print(f"{number3} é o maior número!")
else:
    print("Todos os número são iguais!")