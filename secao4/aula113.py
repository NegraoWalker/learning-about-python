# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

print(multiplica(2,2,2))

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(numero):
    if numero % 2 == 0:
        return print(f"{numero} é par!")
    return print(f"{numero} é ímpar!")

par_ou_impar(3)

