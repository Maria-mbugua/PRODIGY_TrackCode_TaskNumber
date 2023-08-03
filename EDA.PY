# importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
titanic_df = pd.read_csv('C:\\Users\\NJERI\\Downloads\\train (1).csv')

# Vieweing the first few rows of the dataset to understand its structure and variables
titanic_df.head()

# Summary of the dataset
titanic_df.describe()

# Checking for missing values in each column using isnull function
titanic_df.isnull().sum()

# Filling null values with mean age value 29 years old since it's a common average
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)

# Dropping unnecessary columns like Passenger ID, Name, Ticket Number & Cabin number 
titanic_df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Visualizing the survival rate
sns.countplot(x='Survived', data=titanic_df)
plt.show()

# Analyzing the survival rate based on different variables
sns.countplot(x='Survived', hue='Sex', data=titanic_df)
plt.show()

# Examining the distribution of passengers' age
sns.histplot(titanic_df['Age'].dropna(), kde=False)
plt.show()

# Investigating the relationship between fare and survival rate
sns.boxplot(x='Survived', y='Fare', data=titanic_df)
plt.show()
