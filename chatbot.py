import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq  
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import YoutubeLoader

load_dotenv()
llm = ChatGroq(
    model="llama3-8b-8192" 
)

url ='{input}'
loader = YoutubeLoader.from_youtube_url(
    url,
    language=['pt']
)
lista_documentos = loader.load()

documento = ''
for doc in lista_documentos:
    documento = documento + doc.page_content


def resposta_bot(mensagens):
    mensagens_modelo = [('system', 'Você é um assistente divertido chamado BatBot, que usa humor ácido para exemplificar')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | llm
    return chain.invoke({}).content

def carrega_site():
    url_site = input('Digite a url do site: ')
    documento = ''
    return documento

def carrega_pdf():
    documento = ''
    return documento

def carrega_youtube():
    url_youtube = input('Digite a url do vídeo: ')
    documento = ''
    return documento

print('Bem-vindo ao BatBot')

texto_selecao = '''
Digite 1 se você quiser conversar com um site
Digite 2 se você quiser conversar com um PDF
Digite 3 se você quiser conversar com um vídeo do YouTube'''
while True:
    selecao = input(texto_selecao)
    if selecao == '1':
        documento = carrega_site()
        break
    if selecao == '2':
        documento = carrega_pdf()
        break
    if selecao == '3':
        documento = carrega_youtube()
        break
    print('Digite um valor entre 1 e 3')

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