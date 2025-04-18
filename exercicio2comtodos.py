senha = '1234'

password = int(input("Digite sua senha de 4 dígitos: "))

tentativas = 0
while password != senha:
    password = int(input("Senha incorreta. Digite novamente: "))
    tentativas += 1
    if tentativas == 3:
        print("Cartão bloqueado! Contate o suporte\nContato do suporte: 819999-9999")
        break

if password == senha:
    print("Senha correta! Seja bem-vinda(a)!")
