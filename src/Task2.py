import pandas as pd

# Load the dataset from csv
df = pd.read_csv("student_scores.csv")

# Calculate mean, median, and mode
descriptive_stats = {
    "Subject": ["Math", "Science", "English"],
    "Mean": df[["Math", "Science", "English"]].mean().values,
    "Median": df[["Math", "Science", "English"]].median().values,
    "Mode": [df[subject].mode()[0] for subject in ["Math", "Science", "English"]],
}

# Convert to DataFrame and display
desc_stats_df = pd.DataFrame(descriptive_stats)
print(desc_stats_df)


# Calculate variance and standard deviation
descriptive_stats["Variance"] = df[["Math", "Science", "English"]].var().values
descriptive_stats["Standard Deviation"] = df[["Math", "Science", "English"]].std().values

# Convert to DataFrame and display
desc_stats_df = pd.DataFrame(descriptive_stats)
print(desc_stats_df)

