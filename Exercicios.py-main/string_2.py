nome = "chris"
idade = 26
prof = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "chris", "idade": 26}
print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0} Nome: {1} Idade: {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}") #casa decimal :.2f ou .10.2f   