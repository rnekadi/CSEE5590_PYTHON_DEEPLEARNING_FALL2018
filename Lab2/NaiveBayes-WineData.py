# This Program uses the Wine Data from UCI Machine Learning Repository. The is having 13 attribute and 1 Class.
# The purpose of this program is to take Naive Bayes Classification and create Prediction Model and evaluate same.

# Importing pandas,matplotlib ,seaborn, SciKit and Naive Bayes Classifier libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

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

# Fitting Naive Bayes GaussianNB Classification to the Training set with linear kernel

nvclassifier = GaussianNB()
nvclassifier.fit(X_train, Y_train)

# Predicting the Test set results

Y_pred = nvclassifier.predict(X_test)


# Accuracy of NavesBayes on Training Sets using GaussianNB

print('\nAccuracy of Naive Bayes GaussianNB classifier on Training Set: {:.2f}'
     .format(nvclassifier.score(X_train, Y_train)))

# Accuracy of NavesBayes on Testing Sets using GaussianNB

print('\nAccuracy of Naive Bayes GausianNbClassifier on Test Set: {:.2f}'
     .format(nvclassifier.score(X_test, Y_test)))


# print the accuracy score of predicted and actual values on test set using GaussianNB

print('\nAccuracy of the Naive Bayes GaussianNB Classification is on Test Data Prediction: ', metrics.accuracy_score(Y_test, Y_pred))

# Plot the Test Prediction , Test Value on Graph using GaussianNB

plt.scatter(Y_test, Y_pred)

plt.title('NaiveBayesPrediction-GausianNB')

plt.xlabel('True Values')

plt.ylabel('Predictions')

plt.show()









