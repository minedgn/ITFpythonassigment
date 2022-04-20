#!/usr/bin/env python
# coding: utf-8

# In[1]:


#If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a week,
#how much would your $ 1000 reach at the end of the 7th day?

principal = 1000
amount = 1000*((1+(7/100))**7)

print(amount)

