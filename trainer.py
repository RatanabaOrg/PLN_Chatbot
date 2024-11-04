from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from app import chatbot

trainningList = [
    [
        [
            "olá",
            "oi",
            "ajuda",
            "ajudar",
            "qual é o seu nome?",
            "qual seu nome?",
        ],
        "Olá, eu sou a Bety, sua assistente virtual! Como posso ajudar você hoje?"
    ],
    [   
        [
            "acessos mais recentes",
            "acessos recentes",
            "últimos acessos",
            "último acesso",
            "acesso mais recente",
            "acesso recente"
        ],
        
        "Você pode encontrar na página de últimos acessos, localizada no topo do menu lateral à esquerda."
    ],
    [
        [
            "visualizar um usuário",
            "visualizar usuários",
            "visualizar os usuários",
            "visualizar todos os usuários",
            "visualizar todos usuários",
        ],

        "Clique na página de visualizar usuário no final do menu lateral."
    ],
    [
        [
            "áreas cadastradas",
            "visualizar área",
            "visualizar áreas",
            "visualizar todas as áreas",
            "visualizar todas áreas",
        ],

        "Você pode visualizar as áreas cadastradas na página Visualizar, localizada na seção ACESSOS, no menu lateral."
    ],

]

trainer = ListTrainer(chatbot)

for vectors in trainningList:
    for vector in vectors[0]:
        trainer.train([vector, vectors[1]]) 