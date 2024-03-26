# def filtrar_pares(numero):
#     return numero % 2 == 0

# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lista_numeros)

# resultado = filter(filtrar_pares, lista_numeros)
# print(resultado)

# lista_resultado = list(resultado)
# print(lista_resultado)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado_filtro = list(filter(lambda x : x > 5, lista_numeros))
print(resultado_filtro)
