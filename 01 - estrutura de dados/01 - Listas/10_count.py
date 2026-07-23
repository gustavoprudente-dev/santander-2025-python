menu = """
--------------------------------CONTADOR DE 1-------------------------------
Digite quantos números quiser e retornaremos quantas vezes o 1 foi digitado.
----------------------------------------------------------------------------
                    Quantos números você quer analisar?"""
print(menu)

quantos = int(input("                                      "))

numeros = []
for i in range(quantos):
    x = int(input(f"{i+1}° número: "))
    numeros.append(x)

print(numeros.count(1))
