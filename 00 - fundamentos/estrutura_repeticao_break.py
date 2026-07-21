numeros = []

while True: 
    numero = int(input("digite a nota dos alunos:\n(Digite '11' para sair)\n"))
    if numero >= 11:
        break
    numeros.append(numero)

print(numeros, numero, end="  ")