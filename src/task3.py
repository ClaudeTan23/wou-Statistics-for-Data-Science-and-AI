from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
df = pd.read_csv("sustainability_energy_data.csv")

# 3.1 Simple Linear Regression: Area vs Energy Consumption

x_simple = df[['Area (sq. ft.)']].values
y_simple = df['Energy Consumption (kWh)'].values
simple_model = LinearRegression()
simple_model.fit(x_simple,y_simple)
ypred_simple = simple_model.predict(x_simple)
r2_simple = r2_score(y_simple,ypred_simple)
mse_simple = mean_squared_error(y_simple,ypred_simple)
slope_simple = simple_model.coef_
intercept_simple = simple_model.intercept_
print(r2_simple,mse_simple,slope_simple,intercept_simple)

plt.scatter(x_simple,y_simple,color='blue')
plt.plot(x_simple,ypred_simple)
plt.show()



# 3.2 Multiple Linear Regression: Area, Residents, Renewable Energy Usage
x_multiple = df[['Area (sq. ft.)','Number of Residents','Renewable Energy Usage (%)']].values
y_multiple = df['Energy Consumption (kWh)'].values
multiple_model = LinearRegression()
multiple_model.fit(x_multiple,y_multiple)
ypred_multiple = multiple_model.predict(x_multiple)
r2_multiple = r2_score(y_multiple,ypred_multiple)
mse_multiple = mean_squared_error(y_multiple,ypred_multiple)
slope_multiple = multiple_model.coef_
intercept_multiple = multiple_model.intercept_
print(r2_multiple,mse_multiple,slope_multiple,intercept_multiple)

plt.scatter(y_multiple,ypred_multiple)
plt.show()