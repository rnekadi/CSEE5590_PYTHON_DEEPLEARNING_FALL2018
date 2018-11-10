# IMDB Sentiment Analysis using RNN

import os
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Activation, Dense, Embedding, LSTM
from keras import backend as K
from keras.callbacks import TensorBoard
from keras.preprocessing.text import Tokenizer


#print current directory

print(os.getcwd())

# Importing the Dataset and creating the Dataframe

imdb_df = pd.read_csv('./labeledTrainData.tsv', sep = '\t')
pd.set_option('display.max_colwidth', 500)


# Data Tokenization
num_words = 10000
tokenizer = Tokenizer(num_words = num_words)
tokenizer.fit_on_texts( imdb_df.review )


# Encoding
sequences = tokenizer.texts_to_sequences(imdb_df.review)
y = np.array(imdb_df.sentiment)
print(y)

from keras.preprocessing.sequence import pad_sequences
max_review_length = 552
pad = 'pre'
X = pad_sequences(sequences, max_review_length, padding=pad, truncating=pad)

# Training and test Data Creation
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
input_shape = X_train.shape
K.clear_session()

# Model Creation

lstm_model = Sequential()
# We specify the maximum input length to our Embedding layer
# so we can later flatten the embedded inputs

# Embedding
lstm_model.add(Embedding(num_words, 16, input_length=max_review_length))

#
lstm_model.add(LSTM(100))
lstm_model.add(Dense(1))
lstm_model.add(Activation('sigmoid'))
lstm_model.summary()


# Compile Model
lstm_model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])


# Tensoboard Logic


LSTM_DIR = os.getcwd()
tensorboard = TensorBoard(log_dir='LSTM_DIR', histogram_freq=0,
                          write_graph=True, write_images=False)

# Fit the Model

rnn_history = lstm_model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.3,
                            callbacks=[tensorboard], validation_data=(X_test, y_test))


# Evaluating and Loss Analysis

train_score = lstm_model.evaluate(X_test, y_test, verbose=2)
valid_score = lstm_model.evaluate(X_test, y_test, verbose=2)

print('Train MAE: ', round(train_score[1], 4), ', Train Loss: ', round(train_score[0], 4))
print('Val MAE: ', round(valid_score[1], 4), ', Val Loss: ', round(valid_score[0], 4))


# Evaluating and Accuracy and Score

score, accuracy = lstm_model.evaluate(X_test, y_test, verbose=2)

print('Score: %.2f' %(score))
print('Validation Accuracy: %.2f' % (accuracy))



