# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

# def criar_funcao(func):
#     def interna(*args, **kwargs):
#         print('Vou te decorar')
#         for arg in args:
#             e_string(arg)
#         resultado = func(*args, **kwargs)
#         print(f'O seu resultado foi {resultado}.')
#         print('Ok, agora você foi decorada')
#         return resultado
#     return interna


# def inverte_string(string):
#     return string[::-1]


# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('param deve ser uma string')


# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')
# print(invertida)


# def function_decorator(f):
#     def wrapper():
#         print("Iniciada")
#         f()
#         print("Finalizada")
#     return wrapper
    
    
    
# def f1():
#     print("Função f1() chamada!")
    
# def f2():
#     print("Função f2() chamada")


# function_1 = function_decorator(f1)
# function_2 = function_decorator(f2)

# print(function_1)
# print(function_2)

# print(function_1())
# print(function_2())


# def plus_one(number):
#     def add_one(number):
#         return number + 1

#     result = add_one(number)
#     return result



# print(plus_one(4))

# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi

# hello = hello_function()
# print(hello()) #Terminal: "Hi"

# def print_message(message):
#     "Enclosong Function"
#     def message_sender():
#         "Nested Function"
#         print(message)

#     message_sender()

# print_message("Some random message") #Terminal: "Some random message"

# def uppercase_decorator(function):
#     def wrapper():
#         make_uppercase = function().upper()
#         return make_uppercase

#     return wrapper
    
# def say_hi():
#     return 'hello there'

# decorate = uppercase_decorator(say_hi)
# print(decorate()) # Terminal: HELLO THERE


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
    
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi()) # Terminal: HELLO THERE
