import re

'''
You are testing a string through a while loop. The string must pass the following tests or the user must start over, be sure to tell the user the error.

1. String must be at least 10 characters
2. String must contain at least 1 number
3. String must contain at least 1 capital letter
4. String must contain '@' symbol
5. String must contain no spaces

Test data
jdefwkwf - not enough characters
sdnesleuex - at least 10 characters but no number
sdksdjsdf0 - at least 10 characters, contains number, no caps
Sdksdjsdf0 - at least 10 characters, contains number, has caps, no @ symbol
Sd@sdjs df0 - at least 10 characters, contains number, has caps, @ symbol, contains a space
Sd@sdjsdf0 - should pass all tests
'''

# while True:
#     user_input = input("Please enter your string ")
#     print(user_input)
#     break

# #     # Not enough characters

# if len(user_input) >= 10:
#     print(f'Test Passed: {user_input} is greater than 10 characters')
# else:
#     print(f' Test Failed: {user_input} is less thna 10 characters')
  
    
#     # Contain at least 1 number
# print("Lets test for contains 1 number")

#     # Contains at least 1 capital letter
# contains_num = re.search(r'\d' , user_input )
# if contains_num:
#     print(f'Test Passed: {user_input} contains a number')
# else: 
#     print(f'Test Failed: {user_input} does not contain a number')
#     continue

    # Contains '@' symbol
if '@' in user_input:
        print(f'Test Passed: {user_input} contains a \'@' symbol')
    else:
        print(f'Test Failed: {user_input} no a \'@' symbol')
    continue


    # Contains no spaces
    has_space = re.search(r'\s', user_input)
    if not has_space:
        print(f'Test Passed: {user_input} contains no spaces')
        
        



    
    
       
  

    
    