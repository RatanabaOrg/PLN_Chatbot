from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

from chatterbot import ChatBot


chatbot = ChatBot(
    'Training Example',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri="mongodb+srv://ratanabaorg:praga@cluster0.m8qcp.mongodb.net/chatterbot-database?retryWrites=true&w=majority&appName=Cluster0",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe, não entendi. Pode reformular?',
            'maximum_similarity_threshold': 0.50
        }
    ],
    read_only=True
)



trainer = ListTrainer(chatbot)

treinamentos = [
    [
        [
            "olá",
            "oi",
            "ajuda",
            "ajudar",
        ],
        "Olá! Como posso ajudar você hoje?"
    ],
    [
        [
            "qual é o seu nome?",
            "qual seu nome?",
        ],
        "Eu sou a Bety, sua assistente virtual."
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

for treinamento in treinamentos:
    for pergunta in treinamento[0]:
        trainer.train([pergunta, treinamento[1]]) 

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    query = data.get('query')
    
    response = str(chatbot.get_response(query))
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
