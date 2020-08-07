#!/usr/bin/env python
# coding: utf-8

# # 17 list comprehension problems in python

# In[3]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# In[4]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [fruit.upper() for fruit in fruits]
uppercased_fruits


# In[5]:


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
capitalized_fruits


# In[6]:


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if (
    fruit.count("a") + 
    fruit.count("e") + 
    fruit.count("i") + 
    fruit.count("o") + 
    fruit.count("u")) > 2]

fruits_with_more_than_two_vowels


# In[7]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = [fruit for fruit in fruits if (
    fruit.count("a") + 
    fruit.count("e") + 
    fruit.count("i") + 
    fruit.count("o") + 
    fruit.count("u")) == 2]

fruits_with_only_two_vowels


# In[8]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters

[fruit for fruit in fruits if (len(fruit) > 5)]


# In[9]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters

[fruit for fruit in fruits if (len(fruit) == 5)]


# In[10]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters

[fruit for fruit in fruits if (len(fruit) < 5)]


# In[11]:


#Exercise 8 - Make a list containing the number of characters in each fruit. Output would be 5, 4, 10, etc... 

[len(fruit) for fruit in fruits] 


# In[12]:


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if "a" in fruit] 
fruits_with_letter_a


# In[13]:


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

even_numbers = [number for number in numbers if number % 2 == 0]
even_numbers


# In[14]:


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = [number for number in numbers if number % 2 != 0]
odd_numbers


# In[15]:


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = [number for number in numbers if number > 0]
positive_numbers


# In[16]:


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = [number for number in numbers if number < 0]
negative_numbers


# In[19]:


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

[number for number in numbers if number > 9 or number < -9]


# In[20]:


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers_squared = [number ** 2 for number in numbers]
numbers_squared


# In[24]:


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

odd_negative_numbers = [number for number in numbers if number < 0 and number % 2 != 0]
odd_negative_numbers


# In[25]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

numbers_plus_5 = [number + 5 for number in numbers]
numbers_plus_5


# In[34]:


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

def is_prime(num):
    prime_check = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                prime_check = False
                break
        else:
            prime_check = True 
    return prime_check 


# In[35]:


primes= [number for number in numbers if is_prime(number)]
primes

