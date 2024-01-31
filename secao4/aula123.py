pessoa = {
    'nome': 'Walker',
    'sobrenome': 'Negrão'
}

print(pessoa.get('nome'))
print(pessoa.get('altura'))

chave = pessoa.pop('nome')

print(chave)
print(pessoa)

ultimo_chave_valor = pessoa.popitem()

print(ultimo_chave_valor)
print(pessoa)

pessoa.update({
    'nome': 'novo valor',
    'idade': 30,
})

print(pessoa)