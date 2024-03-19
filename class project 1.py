#Variables
username = 'breed'
password = 'Spring_24'


user_input = input("Please enter your username: ")
user_output = input("Please enter your password: ")

username = (user_input == username)
password = (user_output == password)
print(username)
print(password)

if username and password:
     print("Login successful")
else: 
     print('Incorrect username or password')

# # username = input("Please enter your username: ")
# # user_password = input("Please enter your password: ")

# ''' Taken usernames '''
# sample_word = 'black'
# sample_list = ['green', 'blue', 'orange', 'yellow', 'purple']

# # if sample_word in sample_list:
# #     print("Word exists in the list")
# # else:
# #     print("Word does not exist in list")

# userin = ''

# while userin != 'stop':
#     userin = input("Please enter username, or 'stop' to end the loop: ")
#     print(userin)
# while username != user_name and password != user_password:
#      print("Incorrect username or password")
# user_name = input("Please enter your username: ")
# user_password = input("Please enter your password: ")
# print("Login Successful") 

# test_string = 'c1234567'
# At least 8 characters long
# Contains at least one uppercase letter
# one_uppercase = False
# for t in test_string:
#     if t.isupper():
#         one_uppercase = True
# print('Contains at least one uppercase letter? ', one_uppercase)