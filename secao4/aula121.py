# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


pessoa = {
    'nome': 'Walker',
    'sobrenome': 'Negrão'
}

print(len(pessoa))

print(pessoa.keys())
print(list(pessoa.keys())) # Convertendo para list

print(pessoa.values())
print(list(pessoa.values())) # Convertendo para list

print(pessoa.items())
print(list(pessoa.items())) # Convertendo para list

for chave in pessoa:
    print(chave)
