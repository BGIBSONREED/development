'''
You have a variable called hours which equals 24, the number of hours in a day.
Print There are 24 hours in a day. Make sure to use your variable.
First, print using commas. Remember that using commas automatically adds spaces!
Now, print using string concatenation. Remember to cast hours to a string and manually add the spaces!
'''

# hours = 24
# print('There are',hours,'hours in a day.')
# print('There are ' + str(hours) + ' hours in a day.') # concatenation
# print(f'There are {hours} hours in a day.') # f string, or formatted string


'''
Write some code that will print a box around a string.
Examples:
User input: hello
*******
*hello*
*******

User input: programming is fun
********************
*programming is fun*
********************
'''





'''
# You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
# name, which stores the customer's name as a string
# product, which stores the product name as a string
# price, which stores the price of the product as a float
# Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
# Dear {name},
# Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
# We appreciate your business and look forward to serving you again.
# Sincerely,
# The ABC Company
# '''

name = 'Josiah Wilson'
product = 'ABC Sneakers'
price = 74.95343452342

# Remember to format the price



'''
Write some code that takes a string and tells if it is a palindrome (same forwards and backwards).
Hint: Use indexing/slicing and boolean expressions

Examples:
racecar: True
cat: False
'''







''' Loops '''

''' While Loops '''

''' While my start value is less than my end value, we will increment by 1'''



''' While my start value is less than my end value, we will decrement by one - You can stop the infinite loop by hitting ctrl + c'''



''' Example Create a while loop that prints every integer from 1 to 10.'''



'''
While Loops and User Input

While loops are often paired with user input. The condition for the loop might be what the user needs to enter to stop the loop. The user is prompted for input each time it loops, and something happens based on that input.
This allows you to take user input multiple times without writing multiple lines of input(). It also allows the user to control how much input they give.

Lets look at code that will run infinitely until the user tells it to "stop"
'''
# # Initialize our string
# userin = ''

# while userin != 'stop':
#     userin = input("please enter a word, or 'stop' to end the loop: ")
#     print(userin)

'''
Exercise

Improve the login system we wrote last class to allow multiple attempts. You're developing a login system for a website. Write a Python program that checks whether the user has entered the correct username and password. Just like before:
Create two variables called username and password.
Prompt the user to enter their username and password.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
As long as the username and password are incorrect, print “Incorrect username or password”, and keep asking the user for their username and password.
If they match, print “Login successful” and end the program.





'''

# # Set sys id and pass
# sys_id = 'admin'
# sys_password = 'password'

# # Prompt User
# user_id = input("Please enter your username: ")
# user_password = input("Please enter your password: ")

# # Our initial check, while not equal we will enter loop
# while sys_id != user_id and sys_password != user_password:
#         #we have entered the loop, that emans the uswername/pasword did not match
#     print("incorrect username or password")
#     user_id = input("Please enter your username: ")
#     user_password = ("Please enter your password: ")

# print("Login Successful") # Outside of the while loop
    



''' For Loops '''

# # STRING
# my_string = 'Supercalifragilisticexpialidocious'

# for s in my_string:
#     print(s)


# # LIST
# my_list = ['dog', 'cat', 'bird', 'giraffe', 'fox', 'elephant', 'mouse', 'zebra']

# for l in my_list:
#     print(l)

# # TUPLE
# my_tuple = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')

# for months in my_tuple:
#     print(months)


# # DICTIONARY
# my_dictionary = {"First name": "Jill",
#                  "Last name": "Simmons",
#                  "Age": 34,
#                  "Address":"1515 Mockingbird Lane"}

# for keys in my_dictionary.keys():
#     print(keys)

# for values in my_dictionary.values():
#     print(values)

# # SET
# my_set = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

# for days in my_set.set():
#     print(days)


# # RANGE

# for x in range(10,25):
#     print(x)

'''
Write a for loop that loops through a string, counts all the letters, and then print how long the string is.
'''
my_string = 'tomorrow'
count = 0
for s in my_string:

    print(s)
    count += 1 #incrementing count for every letter in string

print(f"There are {count} letters in the word {my_string}")
    


''' Exercise

Take a string from the user. Verify that it's a number.
Write a for loop that adds all the digits together. Then print the total.

Example:
'14253'
15

Hint: remember to cast to int() for each digit in the loop
'''




''' Exercise 
Write some code that will loop through a string and print whether each letter is a vowel or consonant.

Example:
'hello'
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel


'''




''' Exercise 
You're working on a data analysis project for a company that looks at written text. You're only interested in letters from A-Z because you're analyzing language. However, the data you're given has some values that shouldn't be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn't a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.
'''















''' Loops and conditionals '''

'''
What is the difference between a For and While Loop?
How do I write a For Loop?
How do I write a While Loop?

'''
# For Loop
colors = ['green', 'blue', 'orange', 'yellow']



# While Loop




''' Break Keyword '''

# Lets look at the 2 examples below and take note where the loop stops





''' Break in nested loops '''



'''
Exercise

Write some code that takes in numbers from a user one at a time. This should keep going until the user enters 0. Then print the sum of all the numbers.
If the user inputs something that isn't a number, an error message should appear and the program should stop. (Hint: use break)

Example (no error):
5
12
0
Sum: 17

Example (error):
5
7
c
Error: Not a number

'''
'''Declare any needed variables'''




''' Continue keyword '''

''' Example
Use the continue keyword to loop through a string and only print the vowels.
'''
# Option 1


# Option 2



''' 
Exercise:
Sum of Even Digits

Take a string as user input, and verify that it's a number.
Loop through each digit of the number, and only add it to the sum if it's even.
Print the sum of all the even digits at the end. 
Make sure to use the continue keyword.
'''




''' Break, Continue, and Pass '''




'''
Exercise

Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
If the string is empty, stop the loop.
If the string is a number, convert it to a float and add it to a total.
If the string is a set of letters, concatenate to the other letter strings passed in.
If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.


REQUIREMENTS
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.


'''


'''These variables will be placeholders for the total and new string we will be creating'''
    



'''
Exercise

Improve the login system we wrote last class to allow multiple attempts. You're developing a login system for a website. Write a Python program that checks whether the user has entered the correct username and password. Just like before:
Create two variables called username and password.
Prompt the user to enter their username and password.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
As long as the username and password are incorrect, print “Incorrect username or password”, and keep asking the user for their username and password.
If they match, print “Login successful” and end the program.


'''

# Set sys id and pass


# Prompt User


# Our initial check, while not equal we will enter loop



''' For Loops '''

# STRING
my_string = 'Supercalifragilisticexpialidocious'


# LIST
my_list = ['dog', 'cat', 'bird', 'giraffe', 'fox', 'elephant', 'mouse', 'zebra']


# TUPLE
my_tuple = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')



# DICTIONARY
my_dictionary = {"First name": "Jill",
                 "Last name": "Simmons",
                 "Age": 34,
                 "Address":"1515 Mockingbird Lane"}




# SET
my_set = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}



# RANGE



'''
Write a for loop that loops through a string, counts all the letters, and then print how long the string is.
'''



''' Exercise

Take a string from the user. Verify that it's a number.
Write a for loop that adds all the digits together. Then print the total.

Example:
'14253'
15

Hint: remember to cast to int() for each digit in the loop
'''




''' Exercise 
Write some code that will loop through a string and print whether each letter is a vowel or consonant.

Example:
'hello'
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel


'''




''' Exercise 
You're working on a data analysis project for a company that looks at written text. You're only interested in letters from A-Z because you're analyzing language. However, the data you're given has some values that shouldn't be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn't a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.
'''















''' Loops and conditionals '''

'''
What is the difference between a For and While Loop?
How do I write a For Loop?
How do I write a While Loop?

'''
# For Loop
colors = ['green', 'blue', 'orange', 'yellow']



# While Loop




''' Break Keyword '''

# Lets look at the 2 examples below and take note where the loop stops





''' Break in nested loops '''



'''
Exercise

Write some code that takes in numbers from a user one at a time. This should keep going until the user enters 0. Then print the sum of all the numbers.
If the user inputs something that isn't a number, an error message should appear and the program should stop. (Hint: use break)

Example (no error):
5
12
0
Sum: 17

Example (error):
5
7
c
Error: Not a number

'''
'''Declare any needed variables'''




''' Continue keyword '''

''' Example
Use the continue keyword to loop through a string and only print the vowels.
'''
# Option 1


# Option 2



''' 
Exercise:
Sum of Even Digits

Take a string as user input, and verify that it's a number.
Loop through each digit of the number, and only add it to the sum if it's even.
Print the sum of all the even digits at the end. 
Make sure to use the continue keyword.
'''




''' Break, Continue, and Pass '''




'''
Exercise

Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
If the string is empty, stop the loop.
If the string is a number, convert it to a float and add it to a total.
If the string is a set of letters, concatenate to the other letter strings passed in.
If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.


REQUIREMENTS
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.


'''


'''These variables will be placeholders for the total and new string we will be creating'''






