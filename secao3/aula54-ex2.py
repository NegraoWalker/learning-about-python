"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Informe a hora(número inteiro): ")

if hora.isdigit() == True:
    hora_inteira = int(hora)
    if hora_inteira >= 0 and hora_inteira <= 11:
        print("Bom dia!")
    elif hora_inteira >= 12 and hora_inteira <= 17:
        print("Boa tarde!")
    elif hora_inteira >= 18 and hora_inteira <= 23:
        print("Boa noite!")  
else:
    print("Hora digitada não é um número inteiro!")