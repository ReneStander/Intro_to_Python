# Example 1
# Data manipulation

# Import packages
import pandas as pd
import os

os.chdir(r"G:\My Drive\7 Seminars\Python + R workshops\Scripts")
#%%
# Import the data
racing = pd.read_csv("RacingGameData.csv")

#%%
# Obtain the variable names included in the data set
list(racing)

# Obtain the number of observations
racing.shape[0]

# Obtain the number of columns
racing.shape[1]

# Obtain the data types of each column
racing.dtypes

#%%
# Extract the racing tracks column
tracks = racing["Track"]

# Show the unique values in the racing tracks column
track_types = racing["Track"].unique()

#%%
# Subset the data set to only contain the races on the "OvalTrack"
racing_oval = racing.loc[racing["Track"] == "OvalTrack", :]

# Subset the data set to only contain the races on either the "StraightTrack" 
# or the "OvalTrack"
tr = ["StraightTrack", "OvalTrack"]
racing_oval_straight = racing.loc[racing["Track"].isin(tr), :]

# Subset the data set to only contain the races on the "OvalTrack" and
# the car that had a "Bayes" engine
racing_oval_bayes = racing.loc[(racing["Track"] == "OvalTrack") & 
                               (racing["Engine"] == "Bayes"), :]
#%%
# Remove the "TopSpeedReached" column
racing_2 = racing.drop("TopSpeedReached", axis = 1)

# Remove the last 10 observations
racing_reduced = racing[:-10]

#%%
# Create a new variable in the racing data set based on the "FinishTime" variable"
# If FinishTime > 25, the new variable display "slow"
# If FinishTime <= 25, the new variable display "fast"

def slow_fast(time):
    if time > 25:
        return "slow"
    else:
        return "fast"
    
racing["Indicator"] = racing["FinishTime"].apply(slow_fast)


