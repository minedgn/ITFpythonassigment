#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers, 
#converts the entered distance into miles and prints the result

distance = float(input("please enter distance : "))
covn_faktor = 0.621371 
miles = distance * covn_faktor
print("{} distance is {} miles.".format(distance,miles))

