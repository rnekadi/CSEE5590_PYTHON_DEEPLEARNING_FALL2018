# Naive Bayes Classification

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('iris.csv')


# looking at the first 5 values of the dataset

dataset.head()


# Spliting the dataset in independent and dependent variables

X = dataset.iloc[:, :4].values
Y = dataset['class'].values


# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)


# Fitting Naive Bayes Classification to the Training set with linear kernel

from sklearn.naive_bayes import GaussianNB

nvclassifier = GaussianNB()
nvclassifier.fit(X_train, y_train)

# Predicting the Test set results

y_pred = nvclassifier.predict(X_test)

# lets see the actual and predicted value side by side

y_compare = np.vstack((y_test, y_pred)).T

# actual value on the left side and predicted value on the right hand side
# printing the top 5 values

print(y_compare[:5, :])

# import datasets for iris ans metrics

from sklearn import metrics

# print the accuracy score of predicted and actual values on test set

print('\n\nAccuracy of the Naive Bayes Classification is: ', metrics.accuracy_score(y_test, y_pred))

# Plot the Test Prediction , Test Value on Graph

plt.scatter(y_test, y_pred)

plt.xlabel('True Values')

plt.ylabel('Predictions')

plt.show()

