import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset from csv
df = pd.read_csv("student_scores.csv")

# Scatter Plot: Math vs. Science
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Math"], y=df["Science"])
plt.title("Scatter Plot: Math vs. Science Scores")
plt.xlabel("Math Scores")
plt.ylabel("Science Scores")
plt.grid(True)
plt.show()

# Bar Chart: Average Scores
average_scores = df[['Math', 'Science', 'English']].mean()

plt.figure(figsize=(10, 5))
ax = sns.barplot(x=average_scores.index, y=average_scores.values, palette="viridis")
plt.title("Average Scores in Math, Science, and English")
plt.ylabel("Average Score")
plt.xlabel(None)
plt.ylim(0, average_scores.max().max() + 20)
plt.yticks(np.arange(0, average_scores.max().max() + 20, 5))

for bar in ax.containers:
    ax.bar_label(bar, fmt="%.2f", padding=3)
    
plt.show()
