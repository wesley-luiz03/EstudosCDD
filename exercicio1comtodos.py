tentativas = 0
number = int(input("Digite um número para adivinhar: "))

adivinhar = int(input("Digite o número para adivinhar: "))
while adivinhar != number: 
    adivinhar = int(input("Errou! Digite novamente: "))
    tentativas += 1
    if tentativas == 2:
        print("Que triste! Você gastou todas as suas tentativas!")
        break
if adivinhar == number:
    print("Você acertou!")
    