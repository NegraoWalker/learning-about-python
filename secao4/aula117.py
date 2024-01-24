# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def criar_multiplicacao(valor):
    def multiplicaco(x):
        return valor * x
    return multiplicaco


duplicar = criar_multiplicacao(2)
triplicar = criar_multiplicacao(2)
quadruplicar = criar_multiplicacao(2)

print(duplicar(2))
print(triplicar(3))
print(triplicar(4))