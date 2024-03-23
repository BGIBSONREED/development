import re
# Introductory Print statement (rules)
# Thank you for signing up for our website. Please read the rules prior to creating your username and password.
# Username should be lowercase with numbers and underscore only
# Username should not be in the list of taken usernames given. 
# Password should be at least 8 characters long with at least one uppercase letter, lowercase, digit and a special character with no spaces.
# if your password or username does not meet the above requirements you will be prompted with a message to re-enter.



#initialize my variables
username = ''
password = ''

# sys_id = ''
# sys_password = ''

#list to handle error messages
error_messages = ['Username taken', 'Invalid Username', 'Invalid Password']

#Taken Usernames
taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']

# Allowed characters
avail_characters = '!?@#$^&*_-'

#starting loop
while True:
    # username = input('Please enter your username. ')
    password = input('Please enter your password. ')
   
# #Test username
#    # test for taken usernames
   
#     if username in taken_usernames:
#         print(error_messages[0])
#         continue
    
#     # Test for lowercase letter
#     lowercase_letter_test = username[0]
#     teststring = 'breed_24'
 
#     if lowercase_letter_test.isupper():
#         print(error_messages[1])
#         continue


# #test for number
    # contain_numbers = 'breed_24'
             
    # for c in contain_numbers:
    #       if c.isdigit():
    #          print('I am a digit')
    # else:
    #     print('I am not a digit')

# #  test if username has a underscore
    
#     teststring = 'breed_24'
#     my_match = bool(re.search('[_]', teststring))
    # print(my_match) 
 
     
    # avail_characters = '!?@#$^&*_-'
    #test password


# if len(user_output) >= 8:
#     print(f'Test Passed: {user_output} is greater than 8 characters')
# else:
#     print(f' Test Failed: {user_output} is less than 8 characters')



    #authenticate username and password


    #reprompt user to login - this is where I use sys_id/sys_password
    









          

     
# if len(user_output) >= 8:
#     print(f'Test Passed: {user_output} is greater than 8 characters')
# else:
#     print(f' Test Failed: {user_output} is less than 8 characters')

# one_uppercase = False
# for t in user_output:
#     if t.isupper():
#        one_uppercase = True
# print('Contains at least one uppercase letter? ', one_uppercase)

# one_lowercase = False
# for t in user_output:
#     if t.islower():
#        one_lowercase = True
# print('Contains at least one lowercase letter? ', one_lowercase)

# if '_' in user_output:
#     print(f"Test Passed: {user_output} contains a \'_' symbol")    
# else:
#     print(f"Test Failed: {user_output} no a \'_' symbol")

 

