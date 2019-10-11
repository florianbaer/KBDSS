# TF-IDF NO N-Grams
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "He is studying in Rotkreuz",
    "He loves to eat Pizza",
    "He does not live in Rotkreuz",
    "She has a dog",
    "She has a pet"
]

document_names = ['Doc {:d}'.format(i) for i in range(len(documents))]

def get_tfidf(docs, ngram_range=(1,1), index=None):
    vect = TfidfVectorizer(stop_words='english', ngram_range=ngram_range)
    tfidf = vect.fit_transform(documents).todense()
    return pd.DataFrame(tfidf, columns=vect.get_feature_names(), index=index).T

print(get_tfidf(documents, ngram_range=(1,1), index=document_names))