# Usando o método sort():
lista_1 = [4, 7, 1, 6, 3]
print(lista_1) # Antes da ordenação
lista_1.sort() # Ordenando, usando o critério default do método sort
print(lista_1) # Depois da ordenação


lista_2 = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

print(lista_2) # Antes da ordenação
# lista_2.sort() # Não podemos usar o critério default aqui, ocorrerá um erro!

# def ordena_1(elemento): # Criando um critério de ordenação a partir de uma função
#     return elemento['nome'] # Definindo que o critério será a chave nome dos dicionários

# def ordena_2(elemento): # Criando um critério de ordenação a partir de uma função
#     return elemento['nome'] # Definindo que o critério será a chave sobrenome dos dicionários

# lista_2.sort(key=ordena_1) # Passando a função criado como critério para o método sort
# print(lista_2) # Depois da ordenação


lista_2.sort(key=lambda elemento: elemento['sobrenome']) # Passando uma função lambda como critério de comparação entre os elementos(Definindo que o critério será a chave sobrenome dos dicionários)
print(lista_2) # Depois da ordenação

print('##################################################################################################')
# Usando o método sorted():
lista_3 = [11,13,8,55,4]
print(lista_3) # Antes da ordenação
lista_3_ordenada = sorted(lista_3) # Ordenando, usando o critério default do método sorted
print(lista_3_ordenada) # Depois da ordenação


lista_4 = [
    {'nome': 'Walker', 'sobrenome': 'Negrão'},
    {'nome': 'Maria', 'sobrenome': 'Silva'},
    {'nome': 'Daniela', 'sobrenome': 'Moreira'},
    {'nome': 'Luiz', 'sobrenome': 'Lima'},
    {'nome': 'Aline', 'sobrenome': 'Esteves'},
]

print(lista_4) # Antes da ordenação

lista_4_ordenada = sorted(lista_4,key=lambda elemento: elemento['nome']) # Passando uma função lambda como critério de comparação entre os elementos(Definindo que o critério será a chave nome dos dicionários)
print(lista_4_ordenada) # Depois da ordenação