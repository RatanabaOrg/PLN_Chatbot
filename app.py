import re
from flask import Flask, request, jsonify
from flask_cors import CORS  # Importação do CORS
from chatterbot import ChatBot
from trainer import trainningList
from chatterbot.trainers import ListTrainer
from pymongo import MongoClient
import nltk
from nltk.corpus import stopwords
from corrector import correct_phrases

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download("mac_morpho")
stopwords = stopwords.words('portuguese') + ["a", "as", "o", "os", "uma", "um", "umas", "uns", "de", "do", "da", "em", "na", "no", "e", "é"]
stopwords = set(stopwords)

app = Flask(__name__)
CORS(app)  # Habilitar CORS no aplicativo

mongo_uri = "mongodb+srv://ratanabaorg:praga@cluster0.m8qcp.mongodb.net/ratanaba?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client['ratanaba']

if 'statements' in db.list_collection_names():
    db['statements'].drop()

chatbot = ChatBot(
    'Training Example',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri=mongo_uri,
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
    text = text.lower()
    text_without_repeated_chars = re.sub(r'(.)\1+', r'\1\1', text)
    correct_words = correct_phrases(text_without_repeated_chars)
    filtered_words = [word for word in correct_words.split() if word.lower() not in stopwords]
    response = str(chatbot.get_response(' '.join(filtered_words)))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
