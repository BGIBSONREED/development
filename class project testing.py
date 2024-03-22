import re
# Introductory Print statement (rules)




#initialize my variables
username = ''
password = ''

sys_id = ''
sys_password = ''

#list to handle error messages
error_messages = ['Username taken', 'Invalid Username', 'Invalid Password']

#Taken Usernames
taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']



#starting loop
while True:
    username = input('Please enter your username. ')
    # password = input('Please enter your password. ')
   
#test username
    #test for taken usernames
   
    if username in taken_usernames:
        print(error_messages[0])
        continue
    
    #test for lowercase letter
    lowercase_letter_test = username[0]
 
    if lowercase_letter_test.isupper():
        print(error_messages[1])
        continue

    #testing if username has number
    # def contains_number(value):
    #  username = re.findall('[0-9]+', username)
    #  return True if contains_number else False

    username = ''
    if True in [d.isalnum() for d in username]:
        print('The string contains a number')
    else: 
        print(error_messages[1])
        continue

   
    
    # print(error_messages[1])
    # continue

    
# #test for underscore
    

    print('We have passed testing')
    break
    
    #test password



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

 

