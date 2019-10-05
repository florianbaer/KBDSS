from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords 
import nltk

"""
Download tokenizer stuff
"""
nltk.download('punkt')
nltk.download('stopwords')

text = 'When Alexander Graham Bell invented the telephone he had three missed calls from Chuck Norris.'
word_tokens = TreebankWordTokenizer().tokenize(text)
print(word_tokens)

stop_words = set(stopwords.words('english'))
# https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions 
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
print(filtered_sentence) 
