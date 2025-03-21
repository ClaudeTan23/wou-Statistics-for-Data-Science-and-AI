import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
df = pd.read_csv("sustainability_energy_data.csv")

# 1.1 Analyze the dataset for missing or inconsistent data

# Check for missing values
missing_values = df.isnull().sum()
print(missing_values)


# 1.2 Visualize the distribution of energy consumption
plt.figure(figsize=(8, 5))
sns.histplot(df["Energy Consumption (kWh)"], kde=True, color="blue")
plt.title("Distribution of Energy Consumption")
plt.xlabel("Energy Consumption (kWh)")
plt.ylabel("Frequency")
plt.show()

# 1.3 Scatter plot for Area vs Energy Consumption
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Area (sq. ft.)"], y=df["Energy Consumption (kWh)"], color="green", alpha=0.6)
plt.title("Building Size vs Energy Consumption")
plt.xlabel("Area (sq. ft.)")
plt.ylabel("Energy Consumption (kWh)")
plt.show()

# 1.4 Calculate average energy consumption by climate zone
avg_energy_by_zone = df.groupby("Climate Zone")["Energy Consumption (kWh)"].mean()

# Display results
print(avg_energy_by_zone)