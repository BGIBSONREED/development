import re
# Introductory Print statement (rules)

# Thank you for signing up for our website. Please read the rules prior to creating your username and password.
# Username should be lowercase with numbers and underscore only
# Username should not be in the list of taken usernames given. 
# Password should be at least 8 characters long with at least one uppercase letter, lowercase, digit and a special character with no spaces.
# if your password or username does not meet the above requirements you will be prompted with a message to try again



#My Variables
user_name = 'breed_24'
password = 'Spring@2024'
# re_prompt_user =  'breed_24', 'Spring@2024'

# sys_id = 'user_name'
# sys_password = 'user_password'

#list to handle error messages
error_messages = ['Username taken', 'Invalid Username', 'Invalid Password']

#Taken Usernames
taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']

#We are starting the loop


#Testing username has a number
while True:
    contains_num = re.search(r'\d', user_name)

    if contains_num: 
        print(f'Test Passed: {user_name} contains a number')
        
    else: 
        print(f'Test Failed: {user_name} does not contain a number')
        continue
    

#Testing for underscore
    if '@' in user_name:
         print(f'Test Passed: {user_name} contains a \'_\' symbol')
    else:
        print(f'Test Failed: {user_name} \'_\'symbol')
        continue
    

# Test Password
    user_password = input('Please enter your password. ')  
    if len(user_password) >= 8:
        print(f'Test Passed: {user_password} is greater than 8 characters')
        break
    else:
        print(f'Test Failed: {user_password} is less than 8 characters')
        continue
    
# Password contains at least 1 number
    contains_num = re.search(r'\d', user_password)
while True:

    if contains_num: # not sure why this is dotted red
        print(f'Test Passed: {user_password} contains a number')
    else: 
        print(f'Test Failed: {user_password} does not contain a number')
        continue # not sure why this is underlined in red
       

  # Contains at least 1 capital letter
    any_uppercase = any(p.isupper() for p in user_password)
    if any_uppercase:
        print(f'Test passed: {user_password} contains capital letter')
    else:
        print(f'Test Failed: {user_password} has no caps')
        
       # not sure why this underlined in red


 #Contains '@' symbol
    if '@' in user_password:
         print(f'Test Passed: {user_password} contains a \'@\' symbol')
    else:
        print(f'Test Failed: {user_password} \'@\'symbol')
        continue
    

    # # Contains no spaces
    has_space = re.search(r'\s', user_password)

    if not has_space:
        print(f'Test Passed: {user_password} contains no spaces')
        print(f'Login Successful')
        break
    else:
        print(f'Test Failed: {user_password} contains spaces')
        continue

while True:
    re_prompt_user = input('Congraulations on signing up, please login: ')

    if sys_id == re_prompt_user:
        print('Congrautlations on logging in')
        break
    else:
        print("Login has failed please try again")
        continue

