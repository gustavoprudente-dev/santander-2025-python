nome = "Gustavo"
idade = 18
curso = "Engenharia de Software"
dados = {"nome": nome, "idade": idade, "curso": curso}

print("eu tenho %d anos, me chamo %s e curso %s." % (idade, nome, curso))
print("eu tenho {} anos, me chamo {} e curso {}." .format(idade, nome, curso))
print(f"eu tenho {idade} anos, me chamo {nome} e curso {curso}.")
print("eu tenho {nome} anos, me chamo {idade} e curso {curso}.".format(**dados))

saldo = 314.159
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")