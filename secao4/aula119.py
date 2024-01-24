pessoa = {
    'nome':'Walker', 'sobrenome': 'Negrão', 'idade': 30, 'altura': 1.88, 'enderecos': [{'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321}]
}


# print(pessoa, type(pessoa))
# print(pessoa['nome'])
# print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])