#!/usr/bin/env python
# coding: utf-8

# # 1. Conditional Basics

# In[1]:


#a. Prompt the user for a day of the week, print out whether the day is Monday or not
it_is_Monday = True

if it_is_Monday:
    print('I hate Mondays!')


# In[2]:


#b. Prompt the user for a day of the week, print out whether the day is a weekday or a weekend 
it_is_weekday = True

if it_is_weekday:
    print('I have to go to work.')
else:
    print('Party time!')


# In[3]:


#c. Create variables and make up values for:
# The number of hours worked in one week
# The hourly rate
# How much the week's paycheck will be  

#Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked = int(input('How many regular hours did you work? '))
overtime_hours_worked = int(input('How many overtime hours did you work? '))
hourly_pay_rate = 15
weekly_paycheck_regular =  (hours_worked * hourly_pay_rate) 
weekly_paycheck_overtime =  (hours_worked * hourly_pay_rate) + (hourly_pay_rate * 1.5 * overtime_hours_worked)
if hours_worked < 40:
    print("You just earned ", '$', weekly_paycheck_regular)
else :
    print("Your weekly earned paycheck is", '$', weekly_paycheck_overtime)


# # 2. Loop Basics

# In[4]:


#a. While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.    
i = 5
while i <= 15:
    print(i)
    i += 1


# In[5]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
counter = 0
while counter <= 100:
    print(counter)
    counter += 2


# In[6]:


# Alter your loop to count backwards by 5's from 100 to -10.
counter = 100
while counter >= -10:
    print(counter)
    counter -= 5


# In[7]:


# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. 
counter = 2
while counter <= 1000000:
    print(counter)
    counter = counter ** 2


# In[8]:


#Write a loop that uses print to create the output shown below.
counter = 100
while counter >= 5:
    print(counter)
    counter -= 5


# In[9]:


#b. For Loops
#i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
n = int(input("Input a number: "))
for i in range(1,11):
    print(n,'x',i,'=',n*i)


# In[10]:


#ii. Create a for loop that uses print to create the output shown below.
for i in range(10):
    print(str(i) * i)


# In[11]:


#c. Break and Continue  
#i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
   
def get_odd_number_between_1_and_50():
    while True:
        user_number = input("Please input a number between 1 and 50: \n")

        if user_number.isdigit():
            user_number = int(user_number)

            large_enough = user_number > 1
            small_enough = user_number < 50
            odd = user_number % 2 != 0

            if large_enough and small_enough and odd:
                break
            else:
                print("Your input must be less than 50 and odd and greater than: 1\n")
        else:
            print("Your input must be numerals.\n")

    return user_number

user_number = get_odd_number_between_1_and_50()

print(f"Number to skip is: {user_number}")
print() # prints an extra new line

for i in range(1, 50, 2):
    if i == user_number:
        print(f"Yikes! Skipping number: {i}")
        continue
    print(f"Here is an odd number: {i}")


# In[12]:


# d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

user_number = input("Please enter a positive number: ")

if user_number.isdigit():
    user_number = int(user_number)
    if user_number >= 0:
        for i in range(0, user_number + 1):
            print(i)
else: 
    print("Not valid entry")


# In[13]:


#e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

user_number = input("Please enter a positive number: ")

if user_number.isdigit():
    user_number = int(user_number)
    if user_number >= 1:
        for i in reversed(range(1, user_number + 1)):
            print(i)
else: 
    print("Not valid entry")


# # 3. Fizzbuzz

# In[14]:


#One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

#Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

x = 1
a = []
while (x <= 100):
         a.append(x)
         x = x + 1
for i in a:
    if (i % 5 == 0 and i % 3 == 0):
        print ("FizzBuzz")
    elif (i % 5 == 0):
        print("Buzz")
    elif (i % 3 == 0):
        print("Fizz")
    else:
        print(i)


# # 4. Display a table of powers

# In[15]:


# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.  

# Bonus: Research python's format string specifiers to align the table

def square(i):
    return i*i
def cube(i):
    return i*i*i
  
def main():
    start = 1
    end=int(input("What number would you like to go up to? "))
    
    
    print("======\t\t=====\t\t=====")
    print("Number\t\tSquare\t\tCubed")
    print("======\t\t=====\t\t=====")
      
    for i in range(start,end+1):
        print(i,"\t\t",square(i),"\t\t",cube(i))
        
    while True:
        a = input("Do you want to continue? yes/no? ")
        if a=="yes":
            print("Okay, will continue!")
            continue
        elif a=="no":
            print("Okay, will stop!")
            break
        else:
            print("Enter either yes/no")
main()


# # 5. Convert given number grades into letter grades

# In[17]:


# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.  

# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0  

# Bonus
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

user_input = 'yes'
while user_input.lower() == 'yes':
    grade = int(input('Please enter a grade: '))
    if grade >= 99 and grade <= 100:
        print(f'{grade} is an A+')
    elif grade >= 90:
        print(f'{grade} is an A')
    elif grade >= 88:
        print(f'{grade} is an A-')
    elif grade >= 86:
        print(f'{grade} is a B+')
    elif grade >= 82:
        print(f'{grade} is a B')
    elif grade >= 80:
        print(f'{grade} is a B-')
    elif grade >= 78:
        print(f'{grade} is a C+')
    elif grade >= 69:
        print(f'{grade} is a C')
    elif grade >= 67:
        print(f'{grade} is a C-')
    elif grade >= 65:
        print(f'{grade} is a D+')
    elif grade >= 62:
        print(f'{grade} is a D')
    elif grade >= 60:
        print(f'{grade} is a D-')
    elif grade <= 59:
        print(f'{grade} is an F')
    else:
        print('Please enter a grade between 1-100')
    user_input = input('Would you like to continue? yes/no: ')


# # 6. Create a list of dictionaries where each dictionary represents a book that you have read. 

# In[18]:


# Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

# a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

books = [
    {'title': 'The Singularity is Near','author': 'Ray Kurzweil','genre': 'Artificial intelligence/Technology'},
    {'title': 'Rethinking Consciousness','author': 'Michael Graziano','genre': 'Artificial intelligence/Technology'},
    {'title': 'The Righteous Mind','author': 'Jonathan Haidt','genre': 'Ethics'}
]

selected_genre = input('Please enter a genre: ')
selected_books = [book for book in books if book['genre'] == selected_genre]

for book in selected_books:
    print('---')
    print('title: ' + book['title'])
    print('author: ' + book['author'])
    print('genre: ' + book['genre'])

