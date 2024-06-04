# Exercise 3: Loops
# Sum 1 to n

# Import packages
import numpy as np

#%%

n = 1000
sum = 0

for i in np.arange(1,n+1):
    sum += i
    
print(sum)
