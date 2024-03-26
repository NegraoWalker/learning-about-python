# #Exemplo 1: Soma de todos os elementos de uma lista
# from functools import reduce

# lista = [1, 2, 3, 4, 5]

# soma = reduce(lambda x,y: x + y, lista)

# print(soma) 

#Exemplo 2: Multiplicação de todos os elementos de uma lista, a partir de um valor inicial
from functools import reduce

lista = [1, 2, 3, 4, 5]
valor_inicial = 2

resultado = reduce(lambda x,y: x * y, lista, valor_inicial)
# acc = 2 * 1 = 2
# acc = 2 * 2 = 4
# acc = 4 * 3 = 12
# acc = 12 * 4 = 48
# acc = 48 * 5 = 240

print(resultado)

