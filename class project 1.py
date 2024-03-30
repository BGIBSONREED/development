import re
# Introductory Print statement (rules)# Introductory Print statement (rules)

# Thank you for signing up for our website. Please read the rules prior to creating your username and password.
# Username should be lowercase with numbers and underscore only
# Username should not be in the list of taken usernames given. 
# Password should be at least 8 characters long with at least one uppercase letter, lowercase, digit and a special character with no spaces.
# If your password or username does not meet the above requirements you will be prompted with a message to try again

#My Variables
user_name = 'breed_24'
password = 'Spring@2024'
taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']
error_messages = ['Username taken', 'Invalid Username', 'Invalid Password','Invalid username and password']

while True:
    user_name = input('Please enter your username. ')
    user_password = input('Please enter your password. ')

    if user_name in taken_usernames:
        print(error_messages[0])
        continue

#lowercase and uppercase test    
    lowercase_letter_test = user_name[0]
 
    if lowercase_letter_test.isupper():
        print(error_messages[1])
        continue

    any_uppercase = any(p.isupper() for p in user_password)

    if not any_uppercase:
        print(error_messages[2])
        continue
   
    
#contains a number test  

    contains_num = re.search(r'\d', user_name)
    contains_num = re.search(r'\d', user_password)
        
    if not contains_num: 
        print(error_messages[2])
        continue
    
#test length of password
    if len(user_password) >= 8:
        print(f'Test Passed: {user_password} is greater than 8 characters')
    else:
        print(f'Test Failed: {user_password} is less than 8 characters')
        

#testing for character

    if '@' in user_name:
         print(f'Test Passed: {user_name} contains a \'_\',{user_password} \'@\' symbol')
    else:
        print(f'Test Failed: {user_name} contains a \'_\',{user_password} \'@\' symbol')
    

# Contains no spaces
    has_space = re.search(r'\s', user_password)

    if not has_space:
        print(f'Test Passed: {user_password} contains no spaces')
        print(f'Login Successful')
   
    else:
        print(f'Test Failed: {user_password} contains spaces')
        continue

    while True:
     re_prompt = user_name and user_password

     if user_password and user_name == re_prompt:
         print('Login successful')
         break
        

        


     



    
   


    
   
