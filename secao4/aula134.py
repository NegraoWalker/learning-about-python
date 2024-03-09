def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

#Tenho as funções soma e cria_multiplicador e quero transformar as mesmas para lambda:
#soma:
print(executa(lambda x,y:x+y,2,3))
#cria_multiplicador:
duplica = executa(lambda m:lambda n: n * m,2)
print(duplica(2))