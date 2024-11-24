from nltk.corpus import mac_morpho
from collections import Counter
from nltk.metrics import edit_distance

def get_vocabulary():
    words = [word.lower() for word, pos in mac_morpho.tagged_words()]
    return Counter(words)

word_counts = get_vocabulary()
corpus_final = dict(word_counts)


def correct_word(word, corpus):
    if word in corpus:
        return word
    candidates = sorted(corpus.keys(), key=lambda w: (edit_distance(word, w), -corpus[w]))
    return candidates[0] if candidates else word

def correct_phrases(phrase):
    words = phrase.lower().split(" ")
    processed_words = []
    for word in words:
        if word in corpus_final:
            processed_words.append(word)
        else:
            corrected = correct_word(word, corpus_final)
            processed_words.append(corrected)
    return " ".join(processed_words)
