nota = int(input("digite sua nota: "))

if nota < 6 and nota > 3 :
    print("você não atingiu a média, boa sorte na próxima prova!")
elif nota <= 3:
    print("você ficou de recuperação, boa sorte na próxima prova!")
else:
    print("parabéns, você passou!")