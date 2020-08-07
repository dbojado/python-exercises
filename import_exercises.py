#!/usr/bin/env python
# coding: utf-8

# # Exercises

# In[1]:


#1. Import and test 3 of the functions from your functions exercise file.

# Import each function in a different way:
# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name


# In[3]:


import function_exercises
function_exercises.is_two(2)


# In[4]:


from function_exercises import is_vowel
is_vowel("a")


# In[5]:


from function_exercises import is_consonant as ic
ic("a")


# In[6]:


# 2. For the following exercises, 
# read about and use the itertools module from the standard library to help you solve the problem. 

    #1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
    #2. How many different ways can you combine two of the letters from "abcd"?


# In[7]:


import itertools


# In[8]:


(len(list(itertools.product([1,2,3],'abc'))))


# In[9]:


(len(list(itertools.combinations("abcd",2))))


# In[10]:


#3. Save this file as profiles.json inside of your exercises directory. 
# Use the load function from the json module to open this file, it will produce a list of dictionaries. 
# Using this data, write some code that calculates and outputs the following information:

import json
profiles = json.load(open('profiles.json'))


# In[11]:


# Total number of users
len(profiles)


# In[12]:


# Number of active users
len([profile for profile in profiles if profile['isActive']])


# In[13]:


# Number of inactive users
len([profile for profile in profiles if not profile['isActive']])


# In[14]:


# Grand total of balances for all users
def clean_balance(balance):
    balance = balance.replace(',', '')
    balance = balance.replace('$', '')
    return float(balance)


# In[15]:


balances = [profile['balance'] for profile in profiles]
balances = [balance.replace(',', '') for balance in balances]
balances = [balance.replace('$', '') for balance in balances]
balances = [float(balance) for balance in balances]
sum(balances)


# In[16]:


# Average balance per user
sum(balances) / len(balances)


# In[21]:


# User with the lowest balance
user_with_lowest_balance = profiles[0]
for profile in profiles[1:]:
    if clean_balance(profile['balance']) < clean_balance(user_with_lowest_balance['balance']):
        user_with_lowest_balance = profile

user_with_lowest_balance


# In[22]:


# User with the highest balance
user_with_highest_balance = profiles[0]

for profile in profiles[1:]:
    if clean_balance(profile['balance']) > clean_balance(user_with_highest_balance['balance']):
        user_with_highest_balance = profile

user_with_highest_balance


# In[25]:


# Most common favorite fruit
favorite_fruits = [profile['favoriteFruit'] for profile in profiles]
favorite_fruits

fruit_counts = {}

for fruit in favorite_fruits:
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1
max(fruit_counts)


# In[26]:


# Least most common favorite fruit
min(fruit_counts)


# In[27]:


# Total number of unread messages for all users
def extract_digits(s):
    return ''.join([c for c in s if c.isdigit()])

n_unread_messages = [extract_digits(profile['greeting']) for profile in profiles]
sum([int(message) for message in n_unread_messages])

