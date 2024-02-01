#!/usr/bin/env python
# coding: utf-8

# # Selections and Loops

# ## 3.1 Letter Grade Converter
# Create a program that converts number grades to letter grades.
# 
# ### Console:
# ```powershell
# Letter Grade Converter
# 
# Enter numerical grade: 90 
# Letter grade: A
# 
# Continue? (y/n): y
# 
# Enter numerical grade: 88 
# Letter grade: A
# 
# Continue? (y/n): y
# 
# Enter numerical grade: 80 
# Letter grade: B
# 
# Continue? (y/n): y
# 
# Enter numerical grade: 67 
# Letter grade: C
# 
# Continue? (y/n): y
# 
# Enter numerical grade: 59 
# Letter grade: F
# 
# Continue? (y/n): n
# 
# Bye!
# ```
# 
# ### Specifications:
# - Assume that the user will enter valid integers for the grades.
# - The program should continue only if the user enters “y” or “Y” to continue.
# - The grading criteria is as follows:
# 
# | Letter |	Range |
# |---|-------|
# | A |	88-100 |
# | B |	80-87 |
# | C |	67-79 |
# | D |	60-66 |
# | F |	<60 |

# In[25]:


print("Letter Grade Converter", end= "\n")

while True :
    grade = int(input("\nEnter numerical grade: "))
    if grade >= 88 and grade <= 100 :
        print("Letter Grade: A", end="\n\n")
    elif grade < 88 and grade >= 80 :
        print("Letter Grade: B", end="\n\n")
    elif grade < 80 and grade >= 67 :
        print("Letter Grade: C", end="\n\n")
    elif grade < 67 and grade >= 60 :
        print("Letter Grade: D", end="\n\n")
    elif grade < 60 :
        print("Letter Grade: F", end="\n\n")
    
    choice= input("Continue? (y/n): ")
    if choice == "y" or choice == "Y" :
            continue
    elif choice == "n" or choice == "N" :
            break
            
print("\n\nBye")
        


# ## 3.2 - Tip Calculator
# Create a program that calculates three options for an appropriate tip to leave after a meal at a restaurant.
# 
# ### Console
# ```powershell
# Tip Calculator
# 
# Cost of meal: 52.31 
# 
# 15%
# Tip amount:	7.85
# Total amount: 60.16
# 
# 20%
# Tip amount:	10.46
# Total amount: 62.77
# 
# 25%
# Tip amount:	13.08
# Total amount: 65.39
# ```
# 
# ### Specifications:
# - The program should calculate and display the cost of tipping at 15%, 20%, or 25%.
# - Assume the user will enter valid data.
# - The program should round results to a maximum of two decimal places.
# 
# 

# In[39]:


print("Tip Calculator\n")
cost=float(input("Cost of meal: "))
print()

for i in range(15,30,5) :
    perc = i / 100
    tip = cost * perc
    total = tip + cost
    print(i,"%", sep="")
    print("Tip amount: ", round(tip,2))
    print("Total amount: ", round(total,2))


# ## 3.3 - Change Calculator
# Create a program that calculates the coins needed to make change for the specified number of cents.
# 
# ### Console
# ```powershell
# Change Calculator
# 
# Enter number of cents (0-99): 99
# 
# Quarters: 3
# Dimes:	2
# Nickels: 0
# Pennies: 4
# 
# Continue? (y/n): y
# 
# Enter number of cents (0-99): 55
# 
# Quarters: 2
# Dimes:	0
# Nickels: 1
# Pennies: 0
# 
# Continue? (y/n): n 
# 
# Bye!
# ```
# 
# ### Specifications
# - The program should display the minimum number of quarters, dimes, nickels, and pennies that one needs to make up the specified number of cents.
# - Assume that the user will enter a valid integer for the number of cents.
# - The program should continue only if the user enters “y” or “Y” to continue.
# 

# In[3]:


### CODE HERE ###


# ## 3.4 - Table of Powers
# Create a program that displays a table of squares and cubes for the specified range of numbers.
# 
# ### Console
# ```powershell
# Table of Powers
# 
# Start number: 90
# Stop number: 100
# 
# Number	Squared	Cubed
# ======	=======	=====
# 90      8100	729000
# 91      8281	753571
# 92      8464	778688
# 93      8649	804357
# 94      8836	830584
# 95      9025	857375
# 96      9216	884736
# 97      9409	912673
# 98      9604	941192
# 99      9801	970299
# 100     10000	1000000
# ```
# 
# ### Specifications
# - The formulas for calculating squares and cubes are:
# 
#     `square = x ** 2`
#     
#     `cube = x ** 3`
# 
# - Use tabs to align the columns.
# - Assume that the user will enter valid integers.
# - Make sure the user enters a start integer that’s less than the stop integer. If the user enters a start integer that’s greater than the stop integer, display an error message and give the user a chance to enter the integers again.
# 

# In[ ]:


### CODE HERE ###

