total = 0
quantidade = int(input("Digite quantos números você deseja somar: "))

for x in range(quantidade):
    number = int(input(f"Digite o {x + 1}º número: "))
    total += number
    
print(f"A soma de todos os números é: {total}")
