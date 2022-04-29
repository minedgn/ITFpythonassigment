#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number), 
#converts the entered temperature into Fahrenheit degree and prints the result.

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("{} celsius is {} fahrenheit.".format(celsius , fahrenheit))

