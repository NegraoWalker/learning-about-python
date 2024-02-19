#Como declarar conjuntos:
meu_conjunto_vazio = set()
meu_conjunto_1 = {'Chocolate', 1, 3, 4.67, False}
meu_conjunto_2 = set('Abacaxi')

print(type(meu_conjunto_vazio), meu_conjunto_vazio)
print(type(meu_conjunto_1), meu_conjunto_1)
print(type(meu_conjunto_2), meu_conjunto_2)


#Remoção de elementos duplicados de listas:
lista_1 = [1, 2, 3, 3, 3, 3, 4, 5, 6, 7]
conjunto_1 = set(lista_1)
lista_2 = list(conjunto_1)

print(lista_1)
print(lista_2)

#Iteráveis com for, in, not in:
meu_conjunto_1 = {'Chocolate', 1, 3, 4.67, False}
print('Chocolate' in meu_conjunto_1)

for elemento in meu_conjunto_1:
    print(elemento)

print(True not in meu_conjunto_1)

#Métodos mais usados:
meu_conjunto_vazio2 = set()
meu_conjunto_vazio2.add('nome') #adiciona um novo elemento ao conjunto
print(meu_conjunto_vazio2)

meu_conjunto_vazio2.clear() #remove todos os elementos do conjunto
print(meu_conjunto_vazio2)

#Operações em conjuntos:
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1.union(conjunto2)
print(uniao)
intersecao = conjunto1.intersection(conjunto2)
print(intersecao)
diferenca = conjunto1.difference(conjunto2)
print(diferenca)
