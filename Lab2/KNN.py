# KNN is one of the simplest Supervised algorithm mainly used for Classification. It classify data points based on how
# neighbour are classified.Its stores all cases/data point and classify cases/datapoint based on similarity measures.


# Characteristics of a KNN Model
# Fast to create model because it simply stores data
# Slow to predict because many distance calculations
# Can require lots of memory if data set is large


# Lets take Breast Cancer Dataset from UCI ML Repository

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
import pandas as pd
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier

# Importing the dataset

dataset = pd.read_csv('bcdata.csv')


# looking at the first 5 values of the dataset

dataset.head()

# Splitting the dataset in independent and dependent variables

X = dataset.iloc[:, 1:10].values
Y = dataset['Class'].values

# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)


# Fitting KNN Classifier to the Training set with linear kernel

knnclassifier = KNeighborsClassifier(n_neighbors=10)
knnclassifier.fit(X_train, y_train)


# Making the prediction on test data

y_pred = knnclassifier.predict(X_test)


# Calculating Model Accuracy

accuracy = accuracy_score(y_test, y_pred)*100


# Printing the accuracy score of prediction and train test data

print('\nAccuracy of KNN classifier on Training Set: {:.2f}'
     .format(knnclassifier.score(X_train, y_train)))


print('\nAccuracy of KNN classifier on Test Set: {:.2f}'
     .format(knnclassifier.score(X_test, y_test)))

print('\nAccuracy of Prediction :', str(round(accuracy, 2)) + ' %.')


# Now lets understand the Accuracy of KNN on various value of neighbor by creating list of K  for KNN

k_list = list(range(1, 51, 1))

# creating list of cv scores
cv_scores = []

# perform 10-fold cross validation
for k in k_list:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())

# printing klist and cv_score

print(k_list)
print(cv_scores)


# changing to misclassification error
MSE = [1 - x for x in cv_scores]

# Calculating best value of K
best_k = k_list[MSE.index(min(MSE))]
print("The optimal number of neighbors is %d." % best_k)


plt.figure(figsize=(5, 5))
plt.title('The optimal number of neighbors', fontsize=8, fontweight='bold')
plt.xlabel('Number of Neighbors K', fontsize=8)
plt.ylabel('Misclassification Error', fontsize=8)
sns.set_style("whitegrid")
plt.plot(k_list, MSE)

plt.show()


