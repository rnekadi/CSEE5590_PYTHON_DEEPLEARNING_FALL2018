# This Program uses the Wine Data from UCI Machine Learning Repository. The is having 13 attribute and 1 Class.
# The purpose of this program is to plot the Count of Categories on map using seaborn and matplotlib

# Importing pandas,matplotlib and seaborn libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating Dataframe Wine using panda libraries

wine = pd.read_csv('winedata.csv')

# Print the first 5 rows from wine data using head() function

print(wine.head())

# Printing the unique Class from values from csv file

print('The wine data Contains following Unique Class Value:', wine['Class'].unique())

# Describe the wine data
print(wine.describe())

# Plot the Categories in wine data using seaborn and matplotlib

sns.countplot(wine['Class'], label="Count")
plt.show()
