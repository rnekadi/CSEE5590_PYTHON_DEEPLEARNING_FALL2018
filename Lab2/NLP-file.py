# Program to use NLTK libraries and perform various functions

import nltk
import inflect
from nltk.stem import WordNetLemmatizer
from collections import Counter
import re
import string

# Taking the file name from user

x = input('Please enter the file name you want use ?')

# reading the file
with open(x, 'r') as file:
    sentence = file.read()


# NLTP Tokenization of sentence and words


stokens = nltk.sent_tokenize(sentence)
wtokens = nltk.word_tokenize(sentence)


# using the wtokens in to get plurals and singulars using inflect library

inflect = inflect.engine()

singular = []  # Singulars List
plurals = []  # Plurals List

for w in wtokens:
    if inflect.singular_noun(w) is False:
        singular.append(w)
    else:
        plurals.append(w)

print('\nThe Plurals are :', plurals)


# Lemmatization

lemmatizer = WordNetLemmatizer()

lemmar = [lemmatizer.lemmatize(plural) for plural in plurals]

print('\nThe single Lemmars are :', lemmar)

# Bigrams using Sentence Tokenizer

# we need to remove the regular expression from sentences

non_speaker = re.compile('[A-Za-z]+: (.*)')

# Function to remove special character and create bigrams


def extract_phrases(text, phrase_counter, length):
    for sent in nltk.sent_tokenize(text):
        strip_speaker = non_speaker.match(sent)
        if strip_speaker is not None:
            sent = strip_speaker.group(1)
        words = nltk.word_tokenize(sent)
        for phrase in nltk.ngrams(words, length):
            if all(word not in string.punctuation for word in phrase):
                phrase_counter[phrase] += 1


# using the counter for bigrams

phrase_counter = Counter()

# Now taking the sentence tokenizer and genrating phrase Counter
for stoken in stokens:
    extract_phrases(stoken, phrase_counter, 2)


# Printing the Bigram frequency

print('\nThe frequency of bigrams are :', phrase_counter)

most_common_phrases = phrase_counter.most_common(5)

for k, v in most_common_phrases:
    print('\n5 most repeated bigrams are :{0: <5}'.format(v), k)


# searching sentences for 5 most repeated bi grams

bigram = []  # list of 5 most repeated bigram

for k, v in most_common_phrases:
    s = ' '.join(k) # Converting bigram into string as it can be used for search sentence
    bigram.append(s)


fsentence = ''  # Will sentence for top 5 most repeated bigram

for b in bigram:   # looping bigram string one by one
    for s in stokens:  # looping sentence one by one to search bigram string
        if b in s:
            fsentence = fsentence + s


print('\nThe final combined sentence are  below:\n', fsentence)






