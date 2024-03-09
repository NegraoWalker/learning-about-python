pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

for chave, valor in pessoa.items(): #Desempacotamento do dicionário pessoa, forma 1
    print(chave, valor)

pessoas_completa = {**pessoa, **dados_pessoa} #Desempacotamento dos dicionários pessoa e dados_pessoa, forma 2. Nesse caso, tb estamos empacotando o dicionário pessoas_completa
print(pessoas_completa)