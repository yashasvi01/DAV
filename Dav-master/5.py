import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['class'] = iris.target_names[iris.target]

# a. Plot bar chart to show the frequency of each class label in the data.
plt.figure(figsize=(8, 5))
sns.countplot(x='class', data=iris_df)
plt.title('Frequency of Each Class Label in Iris Dataset')
plt.xlabel('Class Label')
plt.ylabel('Frequency')
plt.show()

# b. Draw a scatter plot for Petal width vs Sepal width.
plt.figure(figsize=(8, 5))
sns.scatterplot(x='petal width (cm)', y='sepal width (cm)', hue='class', data=iris_df)
plt.title('Scatter Plot: Petal Width vs Sepal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()

# c. Plot density distribution for feature petal length.
plt.figure(figsize=(8, 5))
sns.kdeplot(data=iris_df, x='petal length (cm)', hue='class', fill=True)
plt.title('Density Distribution: Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Density')
plt.legend()
plt.show()

# d. Use a pair plot to show pairwise bivariate distribution in the Iris Dataset.
sns.set(style="ticks")
sns.pairplot(iris_df, hue='class', markers=["o", "s", "D"])
plt.suptitle('Pairwise Bivariate Distribution in Iris Dataset', y=1.02)
plt.show()
