nota = int(input("digite sua nota: "))

if nota < 6 and nota > 3 :
    print("você não atingiu a média, boa sorte na próxima prova!\n")
elif nota <= 3:
    print("você ficou de recuperação, boa sorte na próxima prova!\n")
else:
    print("parabéns, você passou!\n")