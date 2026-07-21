quantos = int(input("Digite quantas notas serão analisadas: "))
notas = []

for i in range(quantos):
    nota = int(input(f"Nota {i+1}: "))
    notas.append(nota)

print(quantos, notas, nota)