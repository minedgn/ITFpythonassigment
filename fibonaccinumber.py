#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.

def fib(n):

    if n > 1:

        return fib(n-1) + fib(n-2)

    return n

for i in range(11):

    print(fib(i))
    
    
    
    
    

