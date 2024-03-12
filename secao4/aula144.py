# atributos_locais = dir()
# print(atributos_locais)

# minha_lista = [1, 2, 3]
# atributos_lista = dir(minha_lista)
# print(atributos_lista)

# class MinhaClasse:
#     def __init__(self):
#         self.atributo1 = 42
#         self.atributo2 = "Hello"

# minha_instancia = MinhaClasse()
# atributos_classe = dir(MinhaClasse)
# print(atributos_classe)

class Exemplo:
    def __init__(self):
        self.nome = "Exemplo"

objeto = Exemplo()

# Verifica se o objeto possui o atributo 'nome'
if hasattr(objeto, 'nome'):
    print(f"O objeto possui o atributo 'nome': {objeto.nome}")
else:
    print("O objeto não possui o atributo 'nome'")