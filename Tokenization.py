#Satz Tokenizierung:
import nltk
from nltk import tokenize
nltk.download('punkt')

satz = "I am a student at the Hochschule Luzern. I love IT." 
satz = tokenize.sent_tokenize(satz) 
print(satz)

#from nltk import tokenize
wort= "I am a student at the Hochschule Luzern. I love IT." 
token_wort = tokenize.word_tokenize(wort) 
print(token_wort)
