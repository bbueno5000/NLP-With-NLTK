"""
DOCSTRING
"""
import nltk.corpus as corpus
import nltk.tokenize as tokenize

example_sentence = 'This is an example highlighting stop word filtration.'
stop_words = set(corpus.stopwords.words('english'))
word_list = tokenize.word_tokenize(example_sentence)
filtered_sentence = []
for word in word_list:
    if word not in stop_words:
        filtered_sentence.append(word)
print(filtered_sentence)