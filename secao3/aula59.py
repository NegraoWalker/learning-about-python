#Exemplo 1:
# contador = 0

# while contador < 5:
#     print(f"contador: {contador}")
#     contador+=1

#Exemplo 2:
# condicao = True

# while condicao:
#     nome = input("Qual o seu primeiro nome(digite 'sair' para sair do programa)?  ")
#     if nome != "sair":
#         print(f"Seu nome é {nome}")
#     elif nome == "sair":
#         condicao = False
    

# #Exemplo 3:
# while True:
#     nome = input("Qual o seu primeiro nome(digite 'sair' para sair do programa)?  ")
#     if nome != "sair":
#         print(f"Seu nome é {nome}")
#     elif nome == "sair":
#         break

#Exemplo 4:
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        continue #Vai pular o número 6

    if contador >= 10 and contador <= 27:
        continue #Vai pular os números presentes no intervalo de 10 a 27

    print(contador)

    if contador == 40:
        break


print('Acabou')