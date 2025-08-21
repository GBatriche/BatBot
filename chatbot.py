def resposta_bot(mensagens):
    return 'Resposta do bot'

print('Bem vindo ao BatBot (Digite X para sair)\n')

mensagens = []

while True:
    pergunta = input('Usuário: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append({'role': 'user', 'content' : pergunta})
    resposta = resposta_bot(mensagens)
    mensagens.append({'role': 'assistant', 'content': resposta})
    print(f'Bot: {resposta}')
    print('Muito obrigado por usar o BatBot')
    print(mensagens)
