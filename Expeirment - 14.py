import nltk
from nltk.stem import WordNetLemmatizer

def lemmatize_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in nltk.word_tokenize(sentence)]
    return ' '.join(lemmatized_words)

sentence = input("Enter a sentence: ")
lemmatized_sentence = lemmatize_sentence(sentence)
print("Lemmatized Sentence:", lemmatized_sentence)
