soma = 0
number = int(input("Digite um número (0 para sair): "))

while number != 0:
    soma += number
    number = int(input("Digite um número (0 para sair): "))

print(f"Soma total: {soma}")
