# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


contagem = 0
for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}')
    print('Opções: \n')
    valores = pergunta['Opções']
    
    for indice, valor in enumerate(valores):
        print(f'{indice}) {valor}')
    opcao = input('Escolha uma opção: ')
    print('\n')
    opcao = int(opcao)
    if(opcao == 4):
        print('Você acertou!')
        contagem+=1
    elif(opcao == 25):
        print('Você acertou!')
        contagem+=1
    elif(opcao == 5):
        print('Você acertou!')
        contagem+=1
    else:
        print('Você errou! \n')
print()
print(f'Você acertou {contagem} de {len(perguntas)}')