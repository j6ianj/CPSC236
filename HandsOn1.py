#!/usr/bin/env python
# coding: utf-8

# # Chapter 2 - How to write your first program

# ## 2.1 Student Registration
# Create a program that allows a student to complete a registration form and displays a completion message that includes the user’s full name and a temporary password.
# 
# ### Console:
# ```powershell
# Registration Form
# 
# First Name: Eric
# Last Name: Idle
# Birth Year: 1934
# 
# Welcome Eric Idle!
# Your registration is complete!
# Your temporary password is: Eric*1934
# ```
# 
# ### Specifications:
# - The user’s full name consists of the user’s first name, a space, and the user’s last name.
# - The temporary password consists of the user’s first name, an asterisk (*), and the user’s birth year.
# - Assume the user will enter valid data.
# 

# In[25]:


FNAME= str(input("First Name: "))
LNAME= str(input("Last Name: "))
BYEAR= int(input("Birth Year: "))
print("\nWelcome " + FNAME + " " + LNAME + "!")
print("Your registration is complete!")
print("Your temporary password is: "+ FNAME+"*"+str(BYEAR))


# ## 2.2 - Pay Check Calculator
# Create a program that calculates a user’s weekly gross and take-home pay.
# 
# ### Console
# ```powershell
# Pay Check Calculator
# 
# Hours Worked: 35
# Hourly Pay Rate: 14.50
# 
# Gross Pay: 507.5
# Tax Rate: 18%
# Tax Amount: 91.35
# Take Home Pay: 416.15
# ```
# 
# ### Specifications:
# - The formula for calculating gross pay is:
# `gross pay = hours worked * hourly rate`
# - The formula for calculating tax amount is:
# `tax amount = gross pay * (tax rate / 100)`
# - The formula for calculating take home pay is:
# `take home pay = gross pay – tax amount`
# - The tax rate should be 18%, but the program should store the tax rate in a variable so that you can easily change the tax rate later, just by changing the value that’s stored in the variable.
# - The program should accept decimal entries like 35.5 and 14.25.
# - Assume the user will enter valid data.
# - The program should round the results to a maximum of two decimal places.
# 

# In[18]:


print("Pay Check Calculator")
print()
hrs= int(input("Hours Worked: "))
payRate = int(input("Hourly Rate: "))
grossPay = hrs * payRate
print()
print("Gross Pay: " +str(grossPay))
taxRate = 18
taxAmt = grossPay * (taxRate/100)
netPay = grossPay - taxAmt
print("Tax Rate: "+ str(taxRate)+ "%")
print("Tax Amount: "+ str(taxAmt))
print("Take Home Pay: "+ str(netPay))


# ## 2.3 - Travel Time Calculator
# Create a program that calculates the estimated hours and minutes for a trip.
# 
# ### Console
# ```powershell
# Travel Time Calculator
# 
# Enter Miles: 200
# Enter Miles per Hour: 65
# 
# Estimated Travel Time
# Hours: 3
# Minutes: 5
# ```
# 
# ### Specifications
# - The program should only accept integer entries like 200 and 65.
# - Assume that the user will enter valid data.
# 
# ### Hint
# - Use integers with the integer division and modulus operators to get hours and minutes.

# In[24]:


print("Travel Time Calculator")
print()
mileage = int(input("Enter Miles: "))
mph = int(input("Enter MPH: "))
print()
print("Estimated Travel Time")
hrs = mileage//mph
mins = mileage%mph
print("Hours: "+str(hrs))
print("Minutes: "+str(mins))


# In[ ]:




