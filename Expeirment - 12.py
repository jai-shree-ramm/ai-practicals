import nltk
from nltk.stem import PorterStemmer

def stem_sentence(sentence):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in nltk.word_tokenize(sentence)]
    return ' '.join(stemmed_words)

sentence = input("Enter a sentence: ")
stemmed_sentence = stem_sentence(sentence)
print("Stemmed Sentence:", stemmed_sentence)
