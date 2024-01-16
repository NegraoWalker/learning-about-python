"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
lista_nove_digitos_cpf = []
nova_lista_multiplicada = []
for i in range(9):
    numero_cpf = input(f"Digite o {i+1}° número do CPF: ")
    numero_cpf_inteiro = int(numero_cpf)
    lista_nove_digitos_cpf.append(numero_cpf_inteiro)

print(lista_nove_digitos_cpf)

multiplicadores = [10,9,8,7,6,5,4,3,2]
for numero, multiplicador in zip(lista_nove_digitos_cpf,multiplicadores):
    nova_lista_multiplicada.append(numero*multiplicador)
print(nova_lista_multiplicada)

soma_nove_digitos_cpf_inteiros = sum(nova_lista_multiplicada)
print(soma_nove_digitos_cpf_inteiros)

resultado_soma_nove_digitos_cpf_inteiros_por_10 = soma_nove_digitos_cpf_inteiros * 10
print(resultado_soma_nove_digitos_cpf_inteiros_por_10)

resto_divisao_por_11 = resultado_soma_nove_digitos_cpf_inteiros_por_10 % 11

if resto_divisao_por_11 > 9:
    resto_divisao_por_11 = 0

print(resto_divisao_por_11)
