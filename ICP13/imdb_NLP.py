import pandas as pd

from nltk import sent_tokenize
from nltk import word_tokenize


df = pd.read_csv('./imdb_master.csv',encoding='latin-1' )
df['label'] = df['label'].map({'neg': 0, 'pos':1})

review = df['review']


for row in review:
    wtokens = word_tokenize(row)


# lower()
    wtokens = [w.lower() for w in wtokens]

for w in wtokens:
    print(w)


import inflect

inflect = inflect.engine()

singular = []
plurals = []

for w in wtokens:
    if inflect.singular_noun(w) is False:
        singular.append(w)
    else:
        plurals.append(w)

# Lemmatization

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

singles1 = [lemmatizer.lemmatize(plural) for plural in plurals]

print('\nThe single Lemmars are :', singles1)


# Stop Word

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in wtokens if not w in stop_words]
print(words[:100])












