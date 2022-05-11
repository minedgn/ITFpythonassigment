#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Print the prime numbers which are between 1 to entered limit number (n).

for num in range(2,101):

    prime = True

    for i in range(2,num):

        if (num%i==0):

            prime = False

    if prime:

       print (num)

