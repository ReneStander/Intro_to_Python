# Example 2
# Data visualisation

# Import packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.chdir(r"G:\My Drive\7 Seminars\Python + R workshops\Scripts")
racing = pd.read_csv("RacingGameData.csv")

#%%
# Draw a histogram of the FinishTime
sns.histplot(data = racing, x = "FinishTime")
plt.show()

finish = sns.histplot(data = racing, 
                      x = "FinishTime",
                      color = "cyan",
                      edgecolor = "blue",
                      bins = 20)
finish.set(xlabel = "Finish Time (in seconds)", 
           ylabel = "Frequency",
           title = "Histogram of the finish time (in seconds) of all races")
plt.show()

#%%
# Draw a scatterplot of the FinishTime against the TopSpeedReached

scatt = sns.scatterplot(data = racing, 
                        x = "FinishTime",
                        y = "TopSpeedReached",
                        color = "purple")
scatt.set(xlabel = "Finish Time (in seconds)",
          ylabel = "Top Speed Reached (in km per hour)")
plt.show()

#%%
# Draw a scatterplot of the FinishTime against the TopSpeedReached
# Colour the dots according to the Engine used

scatt2 = sns.scatterplot(data = racing, 
                        x = "FinishTime",
                        y = "TopSpeedReached",
                        hue = "Engine",
                        palette=dict(Gauss="#9b59b6", 
                                     Nightingale="#3498db", 
                                     Bayes="#95a5a6"))
scatt2.set(xlabel = "Finish Time (in seconds)",
          ylabel = "Top Speed Reached (in km per hour)")
sns.move_legend(scatt2, "upper left", bbox_to_anchor = (1,1))
plt.show()

#%%
# Draw a boxplot of the FinishTime

box = sns.boxplot(data = racing, 
                  x = "FinishTime",
                  color = "green")
box.set(xlabel = "Finish Time")
plt.show()

#%%
# Draw a boxplot of the Finishtime for each track

box2 = sns.boxplot(data = racing,
                   x = "Track",
                   y = "FinishTime",
                   palette = dict(ComplexTrack = "red",
                                  OvalTrack = "Green",
                                  StraightTrack = "Orange"))
box2.set_xticklabels(["Complex Track", "Oval Track", "Straight Track"])
box2.set(ylabel = "Finish Time")
plt.show()

#%%
# Draw a barplot showing the number of races completed with each type of Track
racing_track = racing["Track"].value_counts()

# Draw a barplot of the vulnerability indices of the birds.
sns.barplot(x=racing_track.index, y=racing_track.values)













