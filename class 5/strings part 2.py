# Strings Part  2

#Strings are immutable 

# str_1 = 'BLUE'
# str_1.lower()
# # print(str_1) # .lower string medthod has not changed string

# str_2 = str_1.lower()
# print(str_2) # new string with lower method

# day = '    TUESDAY    ' # create a new string with no whitespace (this will be sanitizing)
# new_day = day.strip()
# print(len(day))
# print(len(new_day))

# day = day.strip()
# print(day)

# '''indexing, with square brackets'''

# word = Jasmine
# first_letter = word[0]
# print(first_letter)
# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])


# Create a variable to capture the first letter of this string
# greeting = 'hello'
# first_position = greeting[0]
# print(first_position)

# last_position = greeting[len(greeting)-1] #using the len function will allow you to grab the full length

# #using the length and bracket notation, access the last letter in the variable
# month = "February"
# last_position = month[len(month)-1]
# print(last_position)

# # using bracket notation access the letter x, the letter e, and the letter d
# first_name = "Alexander"
# access_letters = first_name[len(access_letters)-2]
# print(access_letters)

#using bracket notation and reverse indexing, access the letter g, the letter i, letter p

fav_season = 'spring'
print(fav_season[-1])
print(fav_season[-3])
print(fav_season[-5])