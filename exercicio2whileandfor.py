number = int(input("Digite um número para saber a tabuada: "))

for x in range(1, 11, 1):
    tabuada = number * x
    print(f"{number} x {x} = {tabuada}")
    