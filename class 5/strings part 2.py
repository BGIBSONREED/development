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

# fav_season = 'spring'
# print(fav_season[-1])
# print(fav_season[-3])
# print(fav_season[-5])

# SLICING

# there are 3 parameters available with indexing with bracket notation [start:stop:step]
fav_food = 'spaghetti'
# slice_of_fav_food = fav_food[2:7] # exclude the character at stop
# print(slice_of_fav_food)

# # using slcing please create a string that accesses 'rica' in 'America'

# country = 'America'
# slice_of_country = country[3:7]
# print(slice_of_country)

# cartoon = 'Dora the explorer'
# slice_of_cartoon = cartoon[1:4]
# print(slice_of_cartoon)

boxer = 'rocky balboa'
# print(boxer[7:11])

# let's step through this string 2 characters at a time
superheroine = 'wonder woman'
# print(superheroine[2:len(superheroine):2])

#lets step through this entire word and skip by 4
word = "supercalifragilisticexpialidocious"
# print(word[0:len(word):4])

"""SLICING IN REVERSE"""

# kids = 'daycare' #excludes the start character
# # print(kids[::-1]) # full daycare in reverse
# print(kids[5:0:-1])
# print(kids[6:0:-1])

#write some code to print the second half of a string
# example: python

# half_string = 'python'
# print(half_string[3:8])

#create a variable to get half of the length of the word

# language = python

# half = (len(language)/2)
