saldo = int(input("Digite o saldo: "))
saque = int(input("Digite o saque: "))

sucesso = True if saldo >= saque else False

if sucesso:
    print("Sucesso no saque!")
else:
    print("Saldo insuficiente.Tente um valor menor")