# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:32:24 2021

@author: PC-ARNAUD
"""
import string
import nltk
import re
import nltk
import numpy as np
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer


def tags_remover(body):
  """
  body: string
  Retourne le corpus sans les balises: "<p> "<code>"
  """
  TAG_RE = re.compile(r'<[^>]+>')
  return TAG_RE.sub('', body)


#print(string.punctuation)
def punctuation_remover(body):
    """
    Remove punctuation inside a string

    Parameters
    ----------
    body : (string)
        corpus of a stackoverflow question.

    Returns
    -------
    (string)
        corpus without punctuation.

    """
    output ="".join([char for char in body if char not in string.punctuation])
    return output



def tokenizer(body):
    """
    Tokenize the body. Convert string input into seperate words

    Parameters
    ----------
    body : (string)
        corpus of a stackoverflow question.

    Returns
    -------
    tokenized : (list)
        list of tokens

    """
    tokenized = word_tokenize(body)
    return tokenized



def stopword_remover(token_arr):
    """
    Remove stopword inside the list of token

    Parameters
    ----------
    token_arr : (list) 
        list of a tokenized string


    Returns
    -------
    result : (list) 
        list of token with the stopword removed

    """
    stop_words = set(stopwords.words("english"))
    result = [token for token in token_arr if not token in stop_words]
    return result


def stemmer(tokenized):
    """
    For each token in the list input, it will keep only the root of the word
    without taking into account its morphology
    ex. "trying -> tri"
    
    Parameters
    ----------
    token_arr : (list)
        list of a tokenized string

    Returns
    -------
    lemmatized : (list)
        list of word lemmatized

    """  
    stemmer_= PorterStemmer()
    result_stem = []
    for token in tokenized:
        #print(stemmer.stem(token))
        result_stem.append(stemmer_.stem(token))
    return result_stem


def lemmatizer(token_arr):
    """
    for each token in the list input, it will keep only the root of the word
    ex. "trying -> try"

    Parameters
    ----------
    token_arr : (list)
        list of a tokenized string

    Returns
    -------
    lemmatized : (list)
        list of word lemmatized

    """  
    lemmatized = []
    lemmatizer_= WordNetLemmatizer()
    for token in token_arr:
        #print(lemmatizer.lemmatize(word))
        lemmatized.append(lemmatizer_.lemmatize(token))
    return lemmatized


def preprocess(body_str):
    """
      Sum up of all technics descrbibed above ! 
      now we just need to feed in the body_text

    Parameters
    ----------
    body_str : (string)
        corpus of one question

    Returns
    -------
    newbody : (string)
        corpus preprocessed

    """

    body_wout_tags = tags_remover(body_str)
    wout_ponct = punctuation_remover(body_wout_tags)
    #Remove non-letters
    wout_ponct = re.sub("[^a-zA-Z]", " ", wout_ponct)
    #warning we stop working on string we work with array of token
    token_vec = tokenizer(wout_ponct)
    token_vec = stopword_remover(token_vec)
    token_vec = stemmer(token_vec)
    token_vec = lemmatizer(token_vec)
    
    newbody = " ".join(token_vec)
    
    return newbody

def td_idf(token_arr):
  """
  Convert token into TD_IDF vector
  """

  from sklearn.feature_extraction.text import TfidfVectorizer

  tfidf_transformer = TfidfVectorizer(ngram_range = (1,3),
                    sublinear_tf = True,
                    max_features = 40000,
                    min_df =10)

  tfidf_transformer.fit_transform(token_arr )
  x_train_tfidf = tfidf_transformer.transform(token_arr)

  return x_train_tfidf, tfidf_transformer
