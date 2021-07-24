import nltk
nltk.download('gutenberg')
corpus = nltk.corpus.gutenberg.fileids()
print(corpus)

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
print(len(emma))