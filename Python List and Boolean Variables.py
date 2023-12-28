#!/usr/bin/env python
# coding: utf-8

# # python data structures and boolean
# - boolean
# - boolean and logical operators
# - Lists
# - comparison operators
# - dictionaries
# - tuples
# - sets

# In[8]:


type(True)


# In[53]:


my_str='khaled alrumaihk'


# In[54]:


my_str.startswith('k')


# In[55]:


print(my_str.isalnum()) #check if all char are numbers
print(my_str.isalpha()) #check if all char in the string are alphabetic
print(my_str.isdigit()) #test if string contains digits
print(my_str.istitle()) #test if string contains title words
print(my_str.isupper()) #test if string contains upper case
print(my_str.islower()) #test if string contains lower case
print(my_str.isspace()) #test if string contains spaces
print(my_str.endswith('k')) #test if string endswith a d
print(my_str.startswith('K')) #test if string startswith H


# ### boolean and logical operators

# In[56]:


True and True


# In[57]:


True and False


# In[58]:


True or False


# In[60]:


True or True


# ### Lists

# In[61]:


type([])


# In[62]:


lst=['Mathematics', 'chemistry', 100, 200, 300, 204]


# In[63]:


type(lst)


# In[64]:


len(lst)


# ### Append

# In[65]:


#.append is used to add elements in the list at the last
lst.append('Khaled')


# In[74]:


lst.append(["John","Bala"])


# In[75]:


lst


# In[68]:


##Indexing in List
lst[3]


# In[73]:


lst[2:7]


# ### Insert

# In[76]:


## insert in a specific order

lst.insert(2,"khaled")


# In[77]:


lst


# ### Extend Method

# In[78]:


lst=[1,2,3,4,5,6]


# In[79]:


lst.extend([8,9])


# In[80]:


lst


# ### Various Operations that we can perform in List

# In[82]:


lst=[1,2,3,4,5]


# In[83]:


sum(lst)


# In[84]:


lst*5


# ### Pop() Method

# In[85]:


lst.pop()


# In[86]:


lst


# In[88]:


lst.pop(0)


# In[89]:


lst


# ### count():Calculates total occurrence of given element of List

# In[90]:


lst=[1,1,2,3,4,5]
lst.count(1)


# In[91]:


#length:Calculates total length of List
len(lst)


# In[94]:


# index(): Returns the index of first occurrence. Start and End index are not necessary parameters
lst.index(1,1,4)


# In[95]:


# min and max
min(lst)


# In[96]:


max(lst)


# 
