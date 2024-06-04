# Example 3
# Exploratory data analysis

import pandas as pd
import os

os.chdir(r"G:\My Drive\7 Seminars\Python + R workshops\Scripts")
racing = pd.read_csv("RacingGameData.csv")

#%%
# Obtain a quick summary of the FinishTime variable
summary = racing["FinishTime"].describe()
summary

#%%
# Average of the FinishTime
racing["FinishTime"].mean()
summary["mean"]

#%%
# Minimum of the FinishTime
print(racing["FinishTime"].min())
print("Minimum: ", summary["min"])

#%%
# Maximum of the FinishTime
print(racing["FinishTime"].max())
print("Maximum: ", summary["max"])

#%%
# Standard deviation of the FinishTime
print(racing["FinishTime"].std())
print("Standard Deviation: ", summary["std"])

#%%
# Median of the FinishTime
print(racing["FinishTime"].median())
print("Median: ", summary["50%"])

#%%
# Interquartile range of the FinishTime
print("Interquartile range: ", summary["75%"] - summary["25%"])


