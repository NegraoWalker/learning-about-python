# Manipulando chaves e valores em dicionários
pessoa = {}

# pessoa['nome'] = "Walker"
# print(pessoa) # Imprime todas as chaves e valores armazenados no dicionário
# print(pessoa['nome']) # Imprime o valor da chave

chave = 'nome' # Criando uma chave dinamicamente
pessoa[chave] = 'Walker'
print(pessoa)


pessoa[chave] = 'João'
print(pessoa)