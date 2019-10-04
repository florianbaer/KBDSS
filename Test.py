from nltk import tag 
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')
nltk.download('wordnet')
tagged_pos = "I am a student at the Hochschule Luzern. I love IT."  
tagged_pos = tag.pos_tag(tagged_pos) 
tagged_pos



#NE Chunking

from nltk import chunk 
tree = chunk.ne_chunk(tagged_pos)
tree

tree.draw()      



#Wort Stemming

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

example_words = ["go","goes","nogo","begone","gone"]

for w in example_words:
    print(ps.stem(w))



#Satz Stemming

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

satz = "I am a student at the Hochschule Luzern. I love IT." 

words = word_tokenize(satz) 

for w in words: print(ps.stem(w))


#Stop Word Removal

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

satz = "I am a student at the Hochschule Luzern. I love IT." 

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(satz)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)


#
#Wort Stemming & Lemmatization

from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()

wort = "going"

print("Stem %s: %s" % ((wort), stemmer.stem((wort))))
print("Lemmatise %s: %s" % ((wort), lemmatiser.lemmatize((wort))))


