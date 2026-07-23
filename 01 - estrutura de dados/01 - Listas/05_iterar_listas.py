notas = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for nota in notas:
    print(nota, end = ".")

print()

for i, nota in enumerate(notas):
    print(f"{nota}, no índice {i}") 