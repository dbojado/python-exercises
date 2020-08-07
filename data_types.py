#!/usr/bin/env python
# coding: utf-8

# # 1. Python Exercise Drills
# Identify the data type of the following values:

# In[2]:


type(99.9)


# In[2]:


type("False")


# In[5]:


type(False)


# In[6]:


type('0')


# In[7]:


type(0)


# In[8]:


type(True)


# In[9]:


type('True')


# In[10]:


type([{}])


# In[13]:


type({'a': []})


# # 2. What data type would best represent:

# A term or phrase typed into a search box?
# String

# If a user is logged in? Boolean

# A discount amount to apply to a user's shopping cart? Float

# Whether or not a coupon code is valid? Boolean

# An email address typed into a registration form? String

# The price of a product? Float

# A Matrix? List

# The email addresses collected from a registration form? List

# Information about applicants to Codeup's data science program? Dictionary

# # 3. Read the expressions
# 

# For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.

# '1' + 2  
# Results in a TypeError: can only concatenate str (not "int") to str

# In[19]:


6 % 4


# In[24]:


type(6 % 4)


# In[25]:


type(type(6 % 4))


# '3 + 4 is ' + 3 + 4  
# Results in a TypeError: can only concatenate str (not "int") to str

# In[27]:


0 < 0


# In[3]:


'False' == False


# In[29]:


True == 'True'


# In[30]:


5 >= -5


# !False or False  
# Results in SyntaxError: invalid syntax; !False is not valid 

# In[54]:


True or "42"


# !True && !False  
# Results in SyntaxError: invalid syntax; !False is not valid   

# In[40]:


6 % 5


# In[41]:


5 < 4 and 1 == 1


# In[42]:


'codeup' == 'codeup' and 'codeup' == 'Codeup'


# 4 >= 0 and 1 !== '1'  
# Results in SyntaxError: invalid syntax; !== is not valid 

# In[44]:


6 % 3 == 0


# In[45]:


5 % 2 != 0


# [1] + 2  
# Results in TypeError: can only concatenate list (not "int") to list

# In[47]:


[1] + [2]


# In[48]:


[1] * 2


# [1] * [2]  
# Results in TypeError: can't multiply sequence by non-int of type 'list'

# In[50]:


[] + [] == []


# {} + {}  
# Results in TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# # 4. Write some Python code 
# Write some Python code, that is, variables and operators, to describe the following scenarios. Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code.

# 1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

# In[92]:


Days_Rented_Little_Mermaid = 3
Days_Rented_Brother_Bear = 5
Days_Rented_Hercules = 1
Price_For_Movie_Per_Day = 3

Total_Days = (Days_Rented_Little_Mermaid + Days_Rented_Brother_Bear + Days_Rented_Hercules)

print (f" ${Price_For_Movie_Per_Day * Total_Days}")


# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

# In[93]:


Google_pay_per_hour = 400 
Amazon_pay_per_hour = 380
Facebook_pay_per_hour = 350

Google_hours_worked = 6
Amazon_hours_worked = 4
Facebook_hours_worked = 10

Total_Google_pay = (Google_pay_per_hour * Google_hours_worked)
Total_Amazon_pay = (Amazon_pay_per_hour * Amazon_hours_worked)
Total_Facebook_pay = (Facebook_pay_per_hour * Facebook_hours_worked)

print (f" ${Total_Google_pay + Total_Amazon_pay + Total_Facebook_pay}")


# 3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

# Class_not_full = True   
# Class_schedule_not_conflict = True  
# 
# Student_can_enroll = Class_not_full and Class_schedule_not_conflict

# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

# bought_more_than_two = False  
# offer_not_expired = True  
# is_premium_member = True  
# 
# offer_valid = offer_not_expired and (bought_more_than_two or is_premium_member)

# # 5. Use the following code to follow the instructions below:
# 
# username = 'codeup'  
# password = 'notastrongpassword'  

# Create a variable that holds a boolean value for each of the following conditions:  
# 
# - the password must be at least 5 characters  
# - the username must be no more than 20 characters  
# - the password must not be the same as the username  
# - bonus neither the username or password can start or end with whitespace  

# at_least_five_characters = len(password) > 5  
# at_least_five_characters

# username_20_characters_or_less = len(username) <20
# 
# password_is_different_from_username = username != password
# 
# username_no_whitespace = username == username.strip()
# password_no_whitespace = password == password.strip()
# 
# username_is_good = username_20_characters_or_less and username_no_whitespace
# password_is_good = at_least_five_characters and password_is_different_from_username and password_no_whitespace
# 
# credentials_are_good = username_is_good and password_is_good
# 
