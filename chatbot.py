import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq  
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatGroq(
    model="llama3-8b-8192" 
)

def resposta_bot(mensagens):
    mensagens_modelo = [('system', 'Você é um assistente divertido chamado BatBot, que usa humor ácido para exemplificar')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | llm
    return chain.invoke({}).content

print('Bem-vindo ao BatBot')

mensagens = []
while True:
    pergunta = input('Usuario: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')

print('Muito obrigado por usar o BatBot')
print(mensagens)