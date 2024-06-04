# Exercise 4: Functions
# Fizz Buzz

# Import packages
import numpy as np

#%%
def FizzBuzz(x):
    if x % 3 == 0 and x % 5 != 0:
        return "Fizz"
    elif x % 5 == 0 and x % 3 != 0:
        return "Buzz"
    elif x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"

#%%

def sum1toN(n):
    sum = 0
    for i in np.arange(1,n+1):
        sum += i
    return sum

sum1toN(6)
sum1toN(10000)
