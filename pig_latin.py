#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Pig Latin Rules
    - if word starts with a vowel, add 'ay' to end
    - if word does not start with a vowel, put first letter at the end, then add 'ay'
        Example:  word --> ordway
        Example:  apple --> appleay
'''

def pig_latin (word):
    first_letter = word[0]
    
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else: 
        pig_word = word[1:] + first_letter + 'ay'
    
    return pig_word


word1 = pig_latin ('word')
word2 = pig_latin ('apple')

print (word1)
print (word2)
pig_latin ('sunny')


# In[ ]:





# In[ ]:




