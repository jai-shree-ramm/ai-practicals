import nltk

def pos_tag_sentence(sentence):
    tagged_words = nltk.pos_tag(nltk.word_tokenize(sentence))
    return tagged_words

sentence = input("Enter a sentence: ")
pos_tags = pos_tag_sentence(sentence)
print("POS Tags:", pos_tags)
