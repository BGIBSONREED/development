# operator_code = 'A987'
# part_id = '49Be'
# item_number = operator_code + part_id
# print(item_number)

# first_name = 'Brenetta'
# last_name = 'Reed'
# full_name = (first_name + ' ' + last_name)
# print(full_name)

# '''multiplication'''
# greeting = 'hip hip horray ' *3
# print(greeting)

# favorite_color = 'blue' *5
# print(favorite_color)


# reference vs value equality == vs is 
# x = 'hello'
# str2 = 'HELLO'.lower()
# print(x)
# print(str2)
# print(x == str2) #lowercase = lowercase is true
# print(x is str2)
# print(id(x))
# print(id(str2))

# test_character = 'b'
# test_string = 'bananas' #is b in bananas
# print(test_character in test_string)

# alphabet = 'abcdefgh'
# length_of_alphabet = len(alphabet)
# print(length_of_alphabet)

# animal = 'elephant'
# length_of_animal = len(animal)
# print(length_of_animal())

# string methods

# word_1 = 'happy' #capitalize me!
# print(word_1.capitalize())

# ex_1 = 'cereal'
# print(ex_1.capitalize())


# word_2 = 'SuPrISe' # make me lower case!
# print(word_2.casefold())
# print('SuPrISe'.casefold())


# word_3 = 'ZOO' # make me lower case!
# print(word_3.casefold())
# print('ZOO'.casefold())

# center string method
# word_4 = 'Good Evening'
# print(word_4)
# print(word_4.center(100)) # takes up 100 characters and centers the string
# print(word_4.center(50))


# ex_4 = 'Hello World!'
# print(word_4.center(65))

# word_5 = 'Pseudopseudohypoparathyroidism' # how many p's?
# print(word_5.count('p'))

# ex_5 = 'Antidisestablishmentarianism' # how many times does the leter 'e' occur?
# print(ex_5.count('e'))

# word_6 = 'I\tam\ta\ttab' # extendtabs ' \ ' is a escape character
# print(word_6)
# print(word_6.expandtabs(10))

# create_new_line = 'I\n am\n a\ n newline'
# print(create_new_line)

# ex_6 = "Let's\t do\t som

# find hte position of the letter k
# word_7 = 'Omphaloskepsis'
# print(word_7.find('k'))

# ex_7 = 'Dichlorodifluoromethane' # find the position of the letter f
# print(ex_7.find('f'))

# word_8 = 'Supercalifragilisticexpialidocious'
# print(word_8.find('g'))

test_1 = "abcdef"
test_2 = '%$123'

print(test_1.isalnum())
print(test_2.isalnum())

ex_8 = '123*' # am I alphanumeric (false due to the asterik)


test_3 = 'abcde'
test_4 = '012345'
print(test_3.isalpha)