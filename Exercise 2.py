# Exercise 2: Conditional statement
# FizzBuzz challenge

x = 5

if x % 3 == 0 and x % 5 != 0:
    print("Fizz")

if x % 5 == 0 and x % 3 != 3:
    print("Buzz")
    
if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
    

#%%
# Nested IF

x = 15

if x % 3 == 0 and x % 5 != 0:
    print("Fizz")
elif x % 5 == 0 and x % 3 != 0:
    print("Buzz")
elif x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
    