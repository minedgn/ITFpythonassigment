#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program that;
#takes a positive integer number from the user,
#checks the entered number if it is Armstrong,
#consider the negative, float and any entries other than numeric values then display a warning message to the user

while True : 

    

    number = input("Enter a positive integer number :")

    digits= len(number)

    summ = 0

    if not number.isdigit() :

        print(number, " is invalid entry. Please enter valid input.")

    elif int(number) >= 0 :

        for i in range(digits) :

            summ = summ + int(number[i])** digits

        if summ == int(number):

            print(number, " is an Armstrong Number.")

            

        else:

            print(number, "is not an Armstrong Number.")

        break

            


