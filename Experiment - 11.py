from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

file = open("Experiment - 11.txt")
passage = file.read()
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(passage)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
print(" ".join(filtered_sentence))
