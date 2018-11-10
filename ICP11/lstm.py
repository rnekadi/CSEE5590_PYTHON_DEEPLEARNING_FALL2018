from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten, LSTM, MaxPooling1D, Dropout, Activation
from keras.layers.embeddings import Embedding

import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)
import nltk
import string
import numpy as np
import pandas as pd
from nltk.corpus import stopwords

from sklearn.manifold import TSNE

df = pd.read_csv('yelp_academic_dataset_review.csv', sep='|', names=['stars', 'text'], error_bad_lines=False)
df = df.dropna()
df = df[df.stars.apply(lambda x:x.isnumeric())]
df = df[df.stars.apply(lambda x:x !="")]
df = df[df.text.apply(lambda x:x !="")]
labels = df.stars.map(lambda x: 1 if int(x)>3 else 0)
import re
def clean_text(text):
    text = text.translate(text.punctuation)
    text = text.lower().split()
    stop = set(stopwords.words('english'))
    text = [w for w in text if not w in stop and len(w)>3]
    text = ' '.join(text)
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)

    text = text.split()
    stemmer = nltk.SnowballStemmer('english')
    stemmed_words = [stemmer.stem(word) for word in text]
    text = ' '.join(stemmed_words)
    return text
df['text'] = df['text'].map(lambda x:clean_text(x))

vocabulary = 2000
tokenizer = Tokenizer(num_words=vocabulary)
tokenizer.fit_on_texts(df['text'])
sequences = tokenizer.texts_to_sequences(df['text'])
data = pad_sequences(sequences,maxlen=50)

print(data)

model = Sequential()
model.add(Embedding(20000,100,input_length=50))
model.add(LSTM(100,dropout=0.2,recurrent_dropout=0.2))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(data,np.array(labels),validation_split=0.4,epochs=3)

word_weights = model.layers[0].get_weights()
word_list = []
for word, i in tokenizer.word_index.items():
    word_list.append(word)

x_embedded = TSNE(n_components=2).fit_transform(word_weights)
number_of_words = 1000
trace = go.Scatter(x = x_embedded[0:number_of_words,0],
                   y = x_embedded[0:number_of_words,1],
                   mode='markers',
                   text=word_list[0:number_of_words])
layout = dict(title = 't-SNE 1 vs t-SNE 2 for sirst 1000 words ',
              yaxis = dict(title='t-SNE 2'),
              xaxis = dict(title='t-SNE 1'),
              hovermode= 'closest')
fig = dict(data = [trace],layout=layout)
py.iplot(fig)

