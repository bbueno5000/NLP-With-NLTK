"""
NOTE: not working dure to missing module
"""
import nltk
import nltk.corpus as corpus
import nltk.stem as stem
import nltk.tokenize as tokenize

nltk.download('all')

def stemming():
    """
    DOCSTRING
    """
    porter_stemmer = stem.PorterStemmer()
    example_words = ['python', 'pythoner', 'pythoning', 'pythoned', 'pythonly']
    for word in example_words:
        print(porter_stemmer.stem(word))

def stop_words():
    """
    DOCSTRING
    """
    example_sentence = 'This is an example highlighting stop word filtration.'
    stopwords = set(corpus.stopwords.words('english'))
    word_list = tokenize.word_tokenize(example_sentence)
    filtered_sentence = []
    for word in word_list:
        if word not in stopwords:
            filtered_sentence.append(word)
    print(filtered_sentence)

if __name__ == '__main__':
    stemming()