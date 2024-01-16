#EXEMPLO DE CPF: 746.824.890-70

lista_nove_digitos_cpf = []
lista_dez_digitos_cpf = []
nova_lista_multiplicada1 = []
nova_lista_multiplicada2 = []


for i in range(10):
    numero_cpf = input(f"Digite o {i+1}° número do CPF: ")
    numero_cpf_inteiro = int(numero_cpf)
    lista_dez_digitos_cpf.append(numero_cpf_inteiro)

lista_nove_digitos_cpf = lista_dez_digitos_cpf[:9]


print(lista_dez_digitos_cpf)
print(lista_nove_digitos_cpf)

multiplicadores1 = [10,9,8,7,6,5,4,3,2]
for numero, multiplicador in zip(lista_nove_digitos_cpf,multiplicadores1):
    nova_lista_multiplicada1.append(numero*multiplicador)

multiplicadores2 = [11,10,9,8,7,6,5,4,3,2]
for numero, multiplicador in zip(lista_dez_digitos_cpf,multiplicadores2):
    nova_lista_multiplicada2.append(numero*multiplicador)


print(nova_lista_multiplicada1)
print(nova_lista_multiplicada2)

soma_nove_digitos_cpf_inteiros = sum(nova_lista_multiplicada1)
soma_dez_digitos_cpf_inteiros = sum(nova_lista_multiplicada2)


print(soma_nove_digitos_cpf_inteiros)
print(soma_dez_digitos_cpf_inteiros)

resultado_soma_nove_digitos_cpf_inteiros_por_10 = soma_nove_digitos_cpf_inteiros * 10
resultado_soma_dez_digitos_cpf_inteiros_por_10 = soma_dez_digitos_cpf_inteiros * 10


print(resultado_soma_nove_digitos_cpf_inteiros_por_10)
print(resultado_soma_dez_digitos_cpf_inteiros_por_10)

resto_divisao_por_11_1 = resultado_soma_nove_digitos_cpf_inteiros_por_10 % 11
resto_divisao_por_11_2 = resultado_soma_dez_digitos_cpf_inteiros_por_10  % 11

if resto_divisao_por_11_1 and resto_divisao_por_11_2 > 9:
    resto_divisao_por_11_1 = 0
    resto_divisao_por_11_2 = 0

print(resto_divisao_por_11_1)
print(resto_divisao_por_11_2)



# lista_nove_digitos_cpf = []
# nova_lista_multiplicada = []
# for i in range(9):
#     numero_cpf = input(f"Digite o {i+1}° número do CPF: ")
#     numero_cpf_inteiro = int(numero_cpf)
#     lista_nove_digitos_cpf.append(numero_cpf_inteiro)

# print(lista_nove_digitos_cpf)

# multiplicadores = [10,9,8,7,6,5,4,3,2]
# for numero, multiplicador in zip(lista_nove_digitos_cpf,multiplicadores):
#     nova_lista_multiplicada.append(numero*multiplicador)
# print(nova_lista_multiplicada)

# soma_nove_digitos_cpf_inteiros = sum(nova_lista_multiplicada)
# print(soma_nove_digitos_cpf_inteiros)

# resultado_soma_nove_digitos_cpf_inteiros_por_10 = soma_nove_digitos_cpf_inteiros * 10
# print(resultado_soma_nove_digitos_cpf_inteiros_por_10)

# resto_divisao_por_11 = resultado_soma_nove_digitos_cpf_inteiros_por_10 % 11

# if resto_divisao_por_11 > 9:
#     resto_divisao_por_11 = 0

# print(resto_divisao_por_11)


# lista_dez_digitos_cpf = []
# nova_lista_multiplicada = []
# for i in range(10):
#     numero_cpf = input(f"Digite o {i+1}° número do CPF: ")
#     numero_cpf_inteiro = int(numero_cpf)
#     lista_dez_digitos_cpf.append(numero_cpf_inteiro)

# print(lista_dez_digitos_cpf)

# multiplicadores = [11,10,9,8,7,6,5,4,3,2]
# for numero, multiplicador in zip(lista_dez_digitos_cpf,multiplicadores):
#     nova_lista_multiplicada.append(numero*multiplicador)
# print(nova_lista_multiplicada)

# soma_dez_digitos_cpf_inteiros = sum(nova_lista_multiplicada)
# print(soma_dez_digitos_cpf_inteiros)

# resultado_soma_dez_digitos_cpf_inteiros_por_10 = soma_dez_digitos_cpf_inteiros * 10
# print(resultado_soma_dez_digitos_cpf_inteiros_por_10)

# resto_divisao_por_11 = resultado_soma_dez_digitos_cpf_inteiros_por_10  % 11

# if resto_divisao_por_11 > 9:
#     resto_divisao_por_11 = 0

# print(resto_divisao_por_11)