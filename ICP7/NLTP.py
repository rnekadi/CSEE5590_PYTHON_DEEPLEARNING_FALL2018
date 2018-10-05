# Getting all text from Website

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)').read()

print(text_from_html(html))

# Writing text into txt file

file = open('output.txt', 'w')

file.write(text_from_html(html))

file.close()


with open('output.txt', 'r') as file:
    sentence = file.read()

# NLTP Tokenization

import nltk

stokens = nltk.sent_tokenize(sentence)
wtokens = nltk.word_tokenize(sentence)

for s in stokens:
    print(s)

for w in wtokens:
    print(w)

# Stemming

# using the wtokens in to get plural using inflect library

import inflect

inflect = inflect.engine()

singular = []
plurals = []

for w in wtokens:
    if inflect.singular_noun(w) is False:
        singular.append(w)
    else:
        plurals.append(w)

print('\n All plurals', plurals)

# Import PoterStemmer
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

singles = [stemmer.stem(plural) for plural in plurals]

print('\nThe single Stemmers are :', singles)



# Lemmatization

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

singles1 = [lemmatizer.lemmatize(plural) for plural in plurals]

print('\nThe single Lemmars are :', singles1)


# POS for this we use wtokens

print('\n The POS are :', nltk.pos_tag(wtokens))

# Named Entity Recognition

from nltk import wordpunct_tokenize, ne_chunk, pos_tag

for sent in nltk.sent_tokenize(sentence):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.wordpunct_tokenize(sent))):
        if hasattr(chunk, 'label'):
            print(chunk.label(), ' '.join(c[0] for c in chunk))

# N-gram using the NLTK in build functions

from collections import Counter


my_bigram = nltk.ngrams(wtokens, 2)

my_trigram = nltk.ngrams(wtokens, 3)

print('\n The bigrams :', Counter(my_bigram))

print('\n The trigram', Counter(my_trigram))



