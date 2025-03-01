import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
file_path = "./student_scores.csv"
df = pd.read_csv(file_path)

# 1. Inferential Statistics

## 1.1 Hypothesis Testing: One-Sample t-test
math_mean = df['Math'].mean()
t_stat, p_value = stats.ttest_1samp(df['Math'], 75)

print("Hypothesis Testing Results:")
print(f"Mean Math Score: {math_mean}")
print(f"T-Statistic: {t_stat:.4f}, P-Value: {p_value:.4f}")

## 1.2 Confidence Interval
confidence = 0.95
ci = stats.t.interval(confidence, len(df['Math'])-1, loc=math_mean, scale=stats.sem(df['Math']))
print(f"\n95% Confidence Interval for Math Scores: {ci}")

## 1.3 Statistical Significance
print("\nThe p-value indicates the probability of observing the test results under the null hypothesis. If p < 0.05, results are statistically significant.")
if p_value < 0.05:
    print("\nReject the null hypothesis: The mean Math score is significantly different from 75.")
else:
    print("\nFail to reject the null hypothesis: No significant difference from 75.")


# 2. Regression Analysis

## 2.1 Simple Linear Regression
X = df[['Math']]
y = df['Science']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

slope = model.coef_[0]
intercept = model.intercept_
rsq = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)

print("\nSimple Linear Regression:")
print(f"Slope: {slope:.4f}, Intercept: {intercept:.4f}")
print(f"R-Squared: {rsq:.4f}, MSE: {mse:.4f}")

# Plot
plt.figure(figsize=(8,6))
sns.scatterplot(x=df['Math'], y=df['Science'], label="Actual")
plt.plot(df['Math'], y_pred, color='red', label="Regression Line")
plt.xlabel("Math Scores")
plt.ylabel("Science Scores")
plt.title("Simple Linear Regression: Math vs Science")
plt.legend()
plt.show()

## 2.2 Multiple Linear Regression
X_multi = df[['Math', 'English']]
y_multi = df['Science']
model_multi = LinearRegression()
model_multi.fit(X_multi, y_multi)
y_multi_pred = model_multi.predict(X_multi)

rsq_multi = r2_score(y_multi, y_multi_pred)
mse_multi = mean_squared_error(y_multi, y_multi_pred)
coefficients = dict(zip(['Math', 'English'], model_multi.coef_))

print("\nMultiple Linear Regression:")
print(f"Coefficients: {coefficients}")
print(f"R-Squared: {rsq_multi:.4f}, MSE: {mse_multi:.4f}")

# Plot Actual vs Predicted
plt.figure(figsize=(8,6))
sns.scatterplot(x=y_multi, y=y_multi_pred)
plt.xlabel("Actual Science Scores")
plt.ylabel("Predicted Science Scores")
plt.title("Actual vs Predicted Science Scores")
plt.show()

## 2.3 Model Evaluation
print("\nModel Comparison:")
print(f"Simple Linear Regression - R-Squared: {rsq:.4f}, MSE: {mse:.4f}")
print(f"Multiple Linear Regression - R-Squared: {rsq_multi:.4f}, MSE: {mse_multi:.4f}")
if rsq_multi > rsq:
    print("Multiple Linear Regression performs better in explaining variance.")
else:
    print("Simple Linear Regression might be preferable due to simplicity.")
