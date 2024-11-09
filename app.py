from flask import Flask, request, jsonify
from chatterbot import ChatBot
from trainer import trainningList
from chatterbot.trainers import ListTrainer
import nltk 
from nltk.corpus import stopwords

nltk.download('punkt_tab')
nltk.download('stopwords')

app = Flask(__name__)

chatbot = ChatBot(
    'Training Example',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri="mongodb+srv://ratanabaorg:praga@cluster0.m8qcp.mongodb.net/ratanaba?retryWrites=true&w=majority&appName=Cluster0",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe, não entendi. Poderia reformular?',
            'maximum_similarity_threshold': 0.50
        }
    ],
    read_only=True
)

trainer = ListTrainer(chatbot)
for vectors in trainningList:
    for vector in vectors[0]:
        trainer.train([vector, vectors[1]]) 



@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    text = data.get('text')
    stop_words = set(stopwords.words('portuguese'))
    text = [word for word in text.split() if word.lower() not in stop_words]
    response = str(chatbot.get_response(' '.join(text)))
    
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
