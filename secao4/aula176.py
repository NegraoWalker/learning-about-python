# def soma_10(elemento):
#     return elemento + 10

# lista_1 = [1,2,3,4,5,6]
# print(lista_1)

# retorno_do_map = map(soma_10,lista_1)
# print(retorno_do_map)

# transforma_em_lista = list(retorno_do_map)
# print(transforma_em_lista)


lista_de_numeros = [1, 2, 3, 4, 5]
resultado_do_map = map(lambda x: x * x, lista_de_numeros)
lista_resultado = list(resultado_do_map)
print(lista_resultado) 