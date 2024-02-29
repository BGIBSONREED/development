'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 
email = input('Hello, please enter your email address: ')

# Clean data
email = email.strip()

# # Test 1: It has a "." at the third-to-last index
test_1 = (email[-4] == '.')
print('Test 1: Does the email have a "." at the third-to-last index?', test_1) 

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier, email cannot be @.com
test_2 = ('@' in email[-6:0:-1])
print('Test 2: Is there a @ symbol in your email? ', test_2)


# ''' in - Returns True if a string appears inside another string (as a substring), and False otherwise.'''
# test_character = 'c'
# test_string = 'bananas'
# print(test_character in test_string)


# kids = 'daycare' #excludes the start character
# print(kids[::-1]) # full daycare in reverse
# print(kids[5:0:-1])
# print(kids[6:0:-1])


# Test 3: There is at least one character before the "@" symbol

# Test 4: It doesn’t have any spaces (doesn’t contain " ") (neta note full string no spaces)

#Final Test with and Keyword
