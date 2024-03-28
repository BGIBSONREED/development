import re
# Introductory Print statement (rules)
# Thank you for signing up for our website. Please read the rules prior to creating your username and password.
# Username should be lowercase with numbers and underscore only
# Username should not be in the list of taken usernames given. 
# Password should be at least 8 characters long with at least one uppercase letter, lowercase, digit and a special character with no spaces.
# if your password or username does not meet the above requirements you will be prompted with a message to re-enter.



#initialize my variables
username = 'breed_24'
password = 'Spring!2024'

sys_id = 'username'
sys_password = 'password'

#list to handle error messages
error_messages = ['Username taken', 'Invalid Username', 'Invalid Password']

#Taken Usernames
taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']

# Allowed characters
avail_characters = ['!','?','@','#','$','^','&','*','_','-']

#starting loop
while True:
    username = input('Please enter your username. ')
    # password = input('Please enter your password. ')  
   
   
# #Test username
  #test for taken usernames
    if username in taken_usernames:
        print(error_messages[0])
        continue
   
      
#testinfg ro
    lowercase_letter_test = username[0]
 
    if lowercase_letter_test.isupper():
        print(error_messages[1])
        continue
    else:
        break

#testing username has a number
result = bool(re.search('[_]', username))

if result:
   print(result)

user_num = username.isidentifier()
if user_num:
    print('Login Successful')
    

 



# '''Test for alphanumeric---unable to get this to run'''
# any_number = any(u.isdecimal() for u in username)
# print('Contains at least one number? ', any_number)

  
# #Testing for password

#  #Has 8 character
# password = input("Please enter password. ")

# if len(password) <= 8:
#     print("Password valid")  
# else:
#     print('invalid') 
    
# #test for number
# # contain_numbers = 'breed_24'
             
# # for c in contain_numbers:
# #      if c.isdigit():
# #       print('I am a digit')
# #      break
# # else:
# #      print('I am not a digit')
# #      continue

# # #  test if username has a underscore
    
 
     
# #avail_characters = '!?@#$^&*_-'
#     #test password

# # testing for length of password
# #     userinput = input("Please enter a password: ")
    
# #     if userinput.isalnum():
# #         print("Error: Not a number")
# #         break
    


# # # Contains no spaces
# # has_space = re.search(r'\s', password)
# # if not has_space:
# #         print(f'Test Passed: {password} contains no spaces')


# #uppercase
# # letter_test = username[0]


# # contains_num = re.search(r'\d' , letter_test)
# # if contains_num:
# #     print(f'Test Passed: {letter_test} contains a number')
   
# # else: 
# #     print(f'Test Failed: {letter_test} does not contain a number')
        


#     #authenticate username and password


#     #reprompt user to login - this is where I use sys_id/sys_password         

     
# # if len(user_output) >= 8:
# #     print(f'Test Passed: {user_output} is greater than 8 characters')
# # else:
# #     print(f' Test Failed: {user_output} is less than 8 characters')

# # one_uppercase = False
# # for t in user_output:
# #     if t.isupper():
# #        one_uppercase = True
# # print('Contains at least one uppercase letter? ', one_uppercase)

# # # one_lowercase = False
# # for t in user_output:
# #     if t.islower():
# #        one_lowercase = True
# # print('Contains at least one lowercase letter? ', one_lowercase)

# # if '_' in user_output:
# #     print(f"Test Passed: {user_output} contains a \'_' symbol")    
# # else:
# #     print(f"Test Failed: {user_output} no a \'_' symbol")

 

