# def outer_function(x):
#     # Esta é a função externa que recebe um parâmetro 'x'

#     def inner_function(y):
#         # Esta é a função interna que recebe um parâmetro 'y'
#         return x + y  # A função interna faz referência à variável 'x' da função externa

#     return inner_function  # Retorna a função interna sem chamá-la

# # Exemplo de uso do closure
# closure_example = outer_function(10)
# result = closure_example(5)

# print(closure_example) # Retorna o endereço da memória da função
# print(result)  # Saída: 15

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# print(falar_bom_dia("Walker"))
# print(falar_boa_noite("Walker"))

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))