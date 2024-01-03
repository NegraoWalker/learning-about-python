"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = "aamoo"
condicao = True
tamanho_palavra_secreta = len(palavra_secreta)
formato_palavra_secreta = "*" * tamanho_palavra_secreta
contagem = 0
letras_acertadas = ""

print("################ JOGO DE ADVINHAR A PALAVRA SECRETA ################")
print("Palavra Secreta: ", "*" * tamanho_palavra_secreta)
while condicao:
    sair = input("Digite 'sair' para finalizar o jogo, 'iniciar' para começar a jogar! ou 'continuar' para continuar a jogar: ")
    if sair == "sair":
        condicao = False
    letra = input("Informe uma letra: ")
    contagem+=1
    letra = letra.lower()
    if len(letra) > 1:
        print("Você informou mais de uma letra!! Por favor informe apenas uma letra!")
    if letra in palavra_secreta:
        letras_acertadas+=letra
    else:
        print("Errou! Tente de novo")
    palavra_secreta_formatada = ""
    for letras in palavra_secreta:
        if letras in letras_acertadas:
            palavra_secreta_formatada+=letras
        else:
            palavra_secreta_formatada+="*"
    print(f"Palavra Secreta: {palavra_secreta_formatada}")
    if palavra_secreta_formatada == palavra_secreta:
        os.system('clear')
        print("Você acertou a palavra secreta!!")
        print(f"Você acertou a palavra com {contagem} tentativas!")
        condicao = False
        