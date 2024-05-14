import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

training_data = [
    ("I love this sandwich.", "positive"),
    ("This is an amazing place!", "positive"),
    ("I feel very good about these beers.", "positive"),
    ("This is my best work.", "positive"),
    ("What an awesome view", "positive"),
    ("I do not like this restaurant", "negative"),
    ("I am tired of this stuff.", "negative"),
    ("I can't deal with this", "negative"),
    ("He is my sworn enemy!", "negative"),
    ("My boss is horrible.", "negative")
]

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    return ' '.join(lemmatized_tokens)

X, y = zip(*training_data)
X = [preprocess_text(text) for text in X]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a pipeline for text classification
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)
new_sentence = "I hate this movie"
preprocessed_sentence = preprocess_text(new_sentence)
prediction = model.predict([preprocessed_sentence])[0]
print("Prediction:", prediction)
