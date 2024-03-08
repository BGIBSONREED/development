'''
Exercise

You're working on a project to develop a login system for a website. The website requires the user to enter a username and password to log in. Write a Python program that checks whether the user entered the correct username and password.
Create two variables called username and password and set them to any valid string values.
Prompt the user to enter their username and password using the input() function.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
If they match, print “Login successful.” If they don't, print “Incorrect username or password.”
'''
''' Exercise solution '''



# Prompt the user to enter their username and password using the input() function.
user_input = input("Please enter your username: ")
user_output = input("Please enter your password: ")
  

# Create two variables called username and password and set them to any valid string values.

username = 'breed'
password = 'week4'


# Create your conditional, includes your comparison

username = (user_input == username)
password = (user_output == password)
print(username)
print(password)


if username and password:
     print("Login successful")
else: 
     print('Incorrect username or password')
