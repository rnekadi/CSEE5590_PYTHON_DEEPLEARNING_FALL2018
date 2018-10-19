from keras.models import Sequential
from keras.layers.core import Dense, Activation
import matplotlib.pyplot as plt

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
dataset = pd.read_csv("housing.csv", header=None).values
# print(dataset)
import numpy as np
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, 0:13], dataset[:, 13],
                                                    test_size=0.25)

my_first_nn = Sequential() # create model
my_first_nn.add(Dense(64, input_dim=13, activation='relu')) # hidden layer 1
# my_first_nn.add(Dense(250, activation='relu')) # hidden layer 2
my_first_nn.add(Dense(64, activation='relu')) # hidden layer 3
my_first_nn.add(Dense(1))  # output layer
my_first_nn.compile(loss='mse', optimizer='RMSProp', metrics=['mae'])
history = my_first_nn.fit(X_train, Y_train, epochs=500, verbose=0,
                                     initial_epoch=0)

print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))


