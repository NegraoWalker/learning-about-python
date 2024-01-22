# def saudacao(msg):
#     return msg

# mensagem = saudacao("Oi sou uma função de primeira classe!!")
# print(mensagem)

# def executa(funcao, msg):
#     return saudacao(msg)

# funcao_executada = executa(saudacao, "Oi fui executada!")
# print(funcao_executada)

def saudacao(msg, nome):
    return f"{msg} para o nome: {nome}"

def executa(funcao, *args): #Empacotando os argumentos em uma tupla
    return saudacao(*args) #Desempacotando os argumentos

funcao_executada = executa(saudacao, "Oi fui executada!", "Walker")
print(funcao_executada)