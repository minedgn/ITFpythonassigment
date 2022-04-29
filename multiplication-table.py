#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##let's write a code that asks the user a number between 1 and 10 and puts that number into the multiplication table.



n= int(input("enter a number between 1-10"))
for i in range(11):
    print('{}*{}=  '.format(n,i),n*i )

