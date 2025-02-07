import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from csv
df = pd.read_csv("student_scores.csv")

# Total number of students
total_students = len(df)

# Probability of Math > 80
prob_math_above_80 = (df["Math"] > 80).sum() / total_students

# Students with Math > 70
students_math_above_70 = df[df["Math"] > 70]

# Probability of Science > 70 given Math > 70
prob_science_above_70_given_math_above_70 = (students_math_above_70["Science"] > 70).sum() / len(students_math_above_70)
print(f"A score above 80 in Math P(Math > 80) = {prob_math_above_80:.2f}")
print(f"A score above 70 in Science, given they scored above 70 in Math P(Science > 70 | Math > 70) = {prob_science_above_70_given_math_above_70:.2f}")

# Define bins and labels
bins = range(50, 101, 10)  # 50-59, 60-69, ..., 90-100
labels = [f"{i}-{i+9}" for i in bins[:-1]]

# Create frequency distribution
math_distribution = pd.cut(df["Math"], bins=bins, labels=labels, right=False).value_counts().sort_index()

print(math_distribution)


# Plot histogram of Math scores
plt.figure(figsize=(8, 5))
sns.histplot(df["Math"], bins=bins, kde=True, color="blue")

plt.title("Distribution of Math Scores")
plt.xlabel("Math Score Range")
plt.ylabel("Frequency")
plt.xticks(bins)  # Set x-axis ticks at bin edges
plt.grid(True)
plt.show()