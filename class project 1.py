#Variables
username = 'breed'
password = 'Spring_24'


user_input = input("Please enter your username: ")
user_output = input("Please enter your password: ")

username = (user_input == username)
password = (user_output == password)
# print(username)
# print(password)


# ''' Taken usernames '''
username = 'breed'
taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']

if username in taken_usernames:
    print("Username taken")
else:
    print("Username successful")


if username:
     print('Login successful')
else: 
     print('Invalid username')

if password:
     print('Login successful')
else: 
     print('Invalid password') 

     
if len(user_output) >= 8:
    print(f'Test Passed: {user_output} is greater than 8 characters')
else:
    print(f' Test Failed: {user_output} is less than 8 characters')

one_uppercase = False
for t in user_output:
    if t.isupper():
       one_uppercase = True
print('Contains at least one uppercase letter? ', one_uppercase)

one_lowercase = False
for t in user_output:
    if t.islower():
       one_lowercase = True
print('Contains at least one lowercase letter? ', one_lowercase)

if '_' in user_output:
    print(f"Test Passed: {user_output} contains a \'_' symbol")    
else:
    print(f"Test Failed: {user_output} no a \'_' symbol")



# userin = ''

# while userin != 'stop':
#     userin = input("Please enter username, or 'stop' to end the loop: ")
#     print(userin)
# while username != user_name and password != user_password:
#      print("Incorrect username or password")
# user_name = input("Please enter your username: ")
# user_password = input("Please enter your password: ")
# print("Login Successful") 

    
# while True:
#     if sys_username == username and sys_password == password:
#         print("Login Successful")
#         break
#     else:
#         print("Incorrect username and password")