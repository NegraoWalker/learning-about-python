"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Informe um número inteiro: ")

if numero.isdigit() == True:
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print("Número é par!")
    else:
        print("Número é ímpar!")
else:
    print("Não é um número inteiro!")