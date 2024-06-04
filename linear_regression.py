# Example 4
# Linear Regression

import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import os

os.chdir(r"G:\My Drive\7 Seminars\Python + R workshops\Scripts")
salary = pd.read_csv("Salary_Data.csv")

#%%
# Split the dataset into the dependent and independent variables
y = salary["Salary"]
x = np.array(salary["YearsExperience"]).reshape(-1,1)

#%%
# Fit the linear regression model

lin_reg = LinearRegression(fit_intercept=True)
lin_reg.fit(x,y)

#%%
# Obtain the coefficients
int = lin_reg.intercept_
slope = lin_reg.coef_

print(f"The intercept parameter for the fitted linear regression line is {round(int,2)}")
print(f"The slope parameter for the fitted linear regression line is {round(slope[0],2)}")

#%%
yhat = lin_reg.predict(x)

# Calculate the Rsquared value
score = r2_score(y, yhat)
print(f"The value of Rsquared is {round(score,4)}")

#%%
sns.scatterplot(data = salary, x = "YearsExperience", y = "Salary")
plt.plot(x, yhat, color = "red", label = rf"$y = {round(int,2)} + {round(slope[0],2)}x$")
plt.xlabel("Years Experience")
plt.legend()
plt.show()
