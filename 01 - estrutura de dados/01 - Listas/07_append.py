listinha = [3, 2, 4, 5]

listinha.append(6)

while True:
    numero = int(input("Digite um número para adicioná-lo à lista\n(0 para sair)\n"))
    if numero == 0:
        break
    listinha.append(numero)
print(listinha) 