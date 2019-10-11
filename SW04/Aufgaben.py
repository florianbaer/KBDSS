import nltk, re, string, collections
from nltk.util import ngrams
text = "I love to read The New York Times when I’m in New York."
tokenized = text.split()
listBigrams = nltk.bigrams(tokenized)
freq_bi = nltk.FreqDist(listBigrams)
fdist = nltk.FreqDist(freq_bi)
for k,v in fdist.items():
    print(k,v)