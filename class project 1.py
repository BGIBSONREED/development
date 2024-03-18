#Variables
username = 'breed'
password = 'spring24'

user_input = input("Please enter your username: ")
user_output = input("Please enter your password: ")

username = (user_input == username)
password = (user_output == password)

if username and password:
     print("Login successful")
else: 
     print('Your username and or password is incorrect please try again')