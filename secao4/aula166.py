# #Forma sem marcação de decorator:
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

#Forma com marcação de decorator:
def function_decorator(f):
    def wrapper():
        print("Iniciada")
        f()
        print("Finalizada")
    return wrapper
    
    
@function_decorator   
def f1():
    print("Função f1() chamada!")

@function_decorator   
def f2():
    print("Função f2() chamada")



print(f1())
print(f2())