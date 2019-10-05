from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

"""
Download nltk stuff
"""
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = 'When Alexander Graham Bell invented the telephone he had three missed calls from Chuck Norris.'
word_tokens = TreebankWordTokenizer().tokenize(text)
print(word_tokens)

stop_words = set(stopwords.words('english'))
# https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions 
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
print(filtered_sentence) 


# stemmed words
ps = PorterStemmer()
stemmed_words = [ps.stem(w) for w in filtered_sentence]
print('Stemmed words:')
print(stemmed_words)

# lemmatized words
lm = WordNetLemmatizer()
lemmatized_words = [lm.lemmatize(w) for w in filtered_sentence]
print('\nLemmatized words:')
print(lemmatized_words)

