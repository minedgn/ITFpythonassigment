#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

#A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard).
#The word will always be a string consisting of only letters from a to z.
#Write a program which returns True if it's a comfortable word or False otherwise.


word = set(input("Please enter word:"))

left = set("qwertaasdfgzxcvb")

right = set("yuiophjklnm")



if word.intersection(left):

  if word.intersection(right):

    print(True)

  else:

   print(False)

elif word.intersection(right):

    print(False)

else:

  print("False")


