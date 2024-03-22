
#testing for number in string

contains_number = 'abd123'

for c in contains_number:
    if c.isdigit():
        print(f'{c}am a digit')
    else:
        print('i am not a digit')


