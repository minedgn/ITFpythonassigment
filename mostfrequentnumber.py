#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Find out the most frequent number and its frequency.

#Write a program that;

#Finds out the most frequent number in the given list.
#Calculates its frequency.
#Prints out the result such as :

numbers = [1, 1, 2, 5 ,6 ,7 ,8 ,4 ,5 ,3 ,5 ,4 ,5 ,4 ,5 ,3, 2, 3 , 4, 5, 6, 4 ,3 , 2 ,4 ,5]

most_common = max(numbers, key = numbers.count)

print("most frequent number is ",most_common, "and it\'s was {} times".format(numbers.count(max(numbers))))

