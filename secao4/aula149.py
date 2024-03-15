#Exemplo 1:
a = 10
b = 0

try:
    result = a/b
except ZeroDivisionError as error: # as variavel -> Armazena detalhes sobre a exceção gerada
    print("Erro:", error)
else:
    print("Executado caso não ocorra exceção!")
finally:
    print("Finalizado!!")


# try:
#     a = 18
#     b = 0
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
# except NameError:
#     print('Nome b não está definido')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexError')
#     print('MSG:', error)
#     print('Nome:', error.__class__.__name__)
# except Exception:
#     print('ERRO DESCONHECIDO.')

# print('CONTINUAR')