# Support Vector Machine  Classification Using Linear Kernel

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

X = dataset.iloc[:, :2].values # taking only first 2 features for our prediction
Y = dataset['class'].values


# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)

# Fitting SVC Classification to the Training set with linear kernel

from sklearn.svm import SVC
svc_linear = SVC(kernel='linear', C=1, gamma=0.5).fit(X_train, y_train)


# Accuracy of SVM Linear kernel on Training set

print('\n\nAccuracy of the SVM Linear Kernel Classification is: ', svc_linear.score(X_train, y_train))


# Accuracy of SVM RBF Kernel on Test Set

print('\n\nAccuracy of the SVM Linear Kernel Classification is: ', svc_linear.score(X_test, y_test))

# Fitting SVC Classification to the Training set with rbf  kernel

from sklearn.svm import SVC
svc_rbf = SVC(kernel='rbf', C=1, gamma=0.5).fit(X_train, y_train)


# Accuracy of SVM Linear kernel on Training set

print('\n\nAccuracy of the SVM RBF Kernel Classification is: ', svc_rbf.score(X_train, y_train))


# Accuracy of SVM RBF Kernel on Test Set

print('\n\nAccuracy of the SVM  RBF Classification is: ', svc_rbf.score(X_test, y_test))


