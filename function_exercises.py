#!/usr/bin/env python
# coding: utf-8

# # Exercises

# In[2]:


#1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    if x == 2 or x == "2":
        return True
    else: 
        return False
    
print(is_two(2))
print(is_two("2"))
print(is_two(3))
print(is_two("3")) 


# In[3]:


#2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(vowel):
    vowels = "aeiouAEIOU"
    if vowel in vowels:
        return True
    else:
        return False
    
print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel("A"))
print(is_vowel("B")) 


# In[4]:


#3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(consonant):
    vowels = "aeiouAEIOU"
    if consonant not in vowels:
        return True
    else:
        return False
    
print(is_consonant("a"))
print(is_consonant("b"))
print(is_consonant("A"))
print(is_consonant("B")) 


# In[5]:


#4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_if_consonant(x):
    vowels = 'aeiouAEIOU'
    for letter in vowels:
        if x[0] in vowels:
            return x
        else:
            return x.capitalize()
        
print(cap_if_consonant("great job!"))


# In[6]:


#5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(x, y):
    bill_total = x
    tip_percentage = y
    tip = bill_total * tip_percentage
    return (f"${tip}")

print(calculate_tip(10, 0.15))


# In[7]:


#6. Define a function named apply_discount. It should accept an original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(x, y):
    original_price = x
    discount_percentage = y
    total = original_price - (original_price * discount_percentage)
    return (f"${total}")

print(apply_discount(10, 0.2))


# In[8]:


#7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(x):
    no_commas = int(x.replace("," , ""))  
    return (no_commas)  

print(handle_commas('1,000,000'))


# In[9]:


#8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if grade >= 100:
        print('Please enter a grade between 0-100')
    elif grade >= 90 :
        print(f'{grade} is an A')
    elif grade >= 80:
        print(f'{grade} is a B')
    elif grade >= 70:
        print(f'{grade} is a C')
    elif grade >= 60:
        print(f'{grade} is a D')
    elif grade <= 59 and grade >=0:
        print(f'{grade} is an F')
    else: 
        print('No negative numbers')
        
get_letter_grade(95)
get_letter_grade(85)
get_letter_grade(75)
get_letter_grade(65)
get_letter_grade(55)
get_letter_grade(0)
get_letter_grade(105)
get_letter_grade(-5)


# In[10]:


#9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in string.lower():
        if x in vowels:
            string = string.replace(x,"")
    return string

print(remove_vowels("Hello Codeup!"))


# In[11]:


#10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores

#for example:
#Name will become name
#First Name will become first_name
#Completed will become completed

def normalize_name(text):
    new_string = (text.strip("0123456789 ").lower().replace(" ", "_"))
    output = ""
    if new_string.isidentifier() == True:
        print(new_string, 'is a valid identifier')
        for i in new_string:
            if i not in "!@#$%^&*()+=-[]{}\/|?.<>,`~":
                output += i
    else: 
        print(new_string, 'is NOT a valid identifier')
    return print(output)

normalize_name("one+one")
normalize_name(" Dani Bojado ") 


# In[12]:


#11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(num_list):
    return [sum(num_list[:i+1]) for i in range(len(num_list))]

print(cumulative_sum([1,1,1]))
print(cumulative_sum([1,2,3,4])) 


# # Bonus

# In[14]:


#1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.


# In[15]:


#2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.

