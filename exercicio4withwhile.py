positivos = 1
x = 1
number = int(input("Digite um número: "))

while x <= number:
    number = int(input("Digite um número: "))
    if number > 0:
        positivos += 1
        
print(f"Total de números positivos: {positivos}")