import nltk, re, string,collections
from nltk.util import ngrams
from nltk.corpus import stopwords, gutenberg

nltk.download('gutenberg')

macbeth = nltk.corpus.gutenberg.raw('shakespeare-macbeth.txt')
macbeth = re.sub('<.*>', '', macbeth)
macbeth = re.sub('ENDOFARTICLE.', '', macbeth)

macbeth_remove = "[" + re.sub("\.", '', string.punctuation) +"]"



