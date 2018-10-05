# This Program uses the Wine Data from UCI Machine Learning Repository. The is having 13 attribute and 1 Class.
# The purpose of this program is to take Naive Bayes Classification and create Prediction Model and evaluate same.

# Importing pandas,matplotlib ,seaborn, SciKit and Support Vector Machine Classifier libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Creating Dataframe Wine using panda libraries

wine = pd.read_csv('winedata.csv')

# Check for Missing Values

print('Check if any column have missing value', wine.isnull().sum())

# Identifying the Correlation of column in wine dataframe using corr() and plotting same using seaborn heatmap
# The Pearson correlation coefficient is a widely used approach that measures the linear dependence between 2 variables.
# The correlation coefficient ranges from -1 to 1. A correlation of 1 is a total positive correlation, a correlation
#  of -1 is a total negative correlation and a correlation of 0 is non-linear correlation.

corr = wine[wine.columns].corr()

sns.heatmap(corr, cmap="YlGnBu", annot=True)

plt.show()

# print correlation

print(corr)

# As we can Column ASH is least correlated we can remove that column from our analysis and get our Features

# Features

X = wine.drop(['Class', 'Ash'], axis=1)

print('\nThe Features are:\n', X.head(2))

# Labels

Y = wine.iloc[:, :1]

print('\nThe Labels:\n', Y.head(2))

# Train-Test Split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Fitting SVC Classification to the Training set with poly kernel

svc_poly = SVC(kernel='poly', degree=4, C=1, gamma=0.1).fit(X_train, Y_train)


# Accuracy of SVM Linear kernel on Training set

print('\n\nAccuracy of the SVM Poly Kernel Classification on Train Data: ', svc_poly.score(X_train, Y_train))


# Accuracy of SVM Linear Kernel on Test Set

print('\n\nAccuracy of the SVM Poly Kernel Classification on Test Data: ', svc_poly.score(X_test, Y_test))

# Fitting SVC Classification to the Training set with rbf  kernel


svc_rbf = SVC(kernel='rbf', C=1, gamma=0.1).fit(X_train, Y_train)


# Accuracy of SVM Linear kernel on Training set

print('\n\nAccuracy of the SVM RBF Kernel Classification on Train Data: ', svc_rbf.score(X_train, Y_train))


# Accuracy of SVM RBF Kernel on Test Set

print('\n\nAccuracy of the SVM  RBF Classification on Test Data: ', svc_rbf.score(X_test, Y_test))