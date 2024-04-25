# print('Imported my name module')

def full_name(firstname, lastname):
    print(firstname, lastname)

def reverse_name(lastname, firstname):
    print(lastname, firstname)
      
def intials(firstname,lastname):

    full_name = input('Type your full name and press ENTER. ')
    initials = ' '.join(name[0].upper() for name in full_name.split())
    print(initials)    


