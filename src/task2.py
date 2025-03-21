from scipy import stats
import pandas as pd

# Load the dataset
df = pd.read_csv("sustainability_energy_data.csv")

# 2.1 Hypothesis Test: Energy Consumption for "Good" vs "Poor" Insulation

# Define groups
good_insulation = df[df["Insulation Type"] == "Good"]["Energy Consumption (kWh)"]
poor_insulation = df[df["Insulation Type"] == "Poor"]["Energy Consumption (kWh)"]

# Perform independent t-test (assuming unequal variances)
t_stat, p_value = stats.ttest_ind(good_insulation, poor_insulation, equal_var=False)
print(f"{t_stat}, {p_value}")

# 2.2 Confidence Interval for buildings with renewable energy usage >50%
renewable_buildings = df[df["Renewable Energy Usage (%)"] > 50]["Energy Consumption (kWh)"]
confidence_interval = stats.t.interval(
    0.95, len(renewable_buildings) - 1, loc=renewable_buildings.mean(), scale=stats.sem(renewable_buildings)
)

print(confidence_interval)