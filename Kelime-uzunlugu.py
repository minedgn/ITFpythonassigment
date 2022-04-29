#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#girilen kelimenin uzunlugunu veren program


sentence = input("Give me a sentence. : ") 
                 
word_list = sentence.split()
longest = 0
i = 0
while i < len(word_list) :
    if len(word_list[i]) > longest:
     longest = len(word_list[i])
    i += 1
print("Teha length of the longest word  :", longest)

