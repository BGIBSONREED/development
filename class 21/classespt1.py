from datetime import datetime
import datetime

'''
Classes
'''
# Class Definition and Initializer
class Point2d:

#string initializer
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

#string representation
    def __str__(self):
        return f'({self.x},{self.y})'
    
#add your object to another object of your class
    def __add__(self, other):  
        return Point2d(self.x + other.x, self.y + other.y) 
        
#subtract my object from another object
    def __sub__(self, other):  
        return Point2d(self.x - other.x, self.y - other.y) 
    
#test equality between this object and another  
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
          return True
        return False
    
#less than function
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
          return True
        return False

#The mutator or setter method- changes the x and y of our objects
    #mutator for x
    def set_x(self, new_x):
        self.x = new_x

    #mutator for y
    def set_y(self, new_y):
        self.y = new_y

    #accessor method for x
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

#creating the object of the Point2d Class    
# point1 = Point2d(4,10)
# point2 = Point2d(5,9)
     

# Return a string representation of this object
# print(point1) 
# print(point2)   
    
# Adds this object to another object from the same class, return a new object.
# print(point1+point2)
    
# Subtracts another object from this object, return a new object.
# print(point1-point2)

# Test equality between this object and another, return a boolean.
point3 = Point2d(3,4)
point4 = Point2d(3,4)
# print(point3 == point4)

#Less than function
point5 = Point2d(10,12)
point6 = Point2d(13,15)
# print(point5 < point6)
     
    
# Mutator method
point7 = Point2d(5,11)
point7.set_x(10)
# print(point7)

point7.set_y(25)
# print(point7)
  
# Accessor method
# print(point7.get_x())
# print(point7.get_y())

'''Exercise - Dog Class
This class will take 3 parameters, dog name, dog breed, and age (human years)'''

class Dog:

    #initializer
    def __init__(self, name, breed, birth_year):
        self.name = name
        self.breed = breed
        self.birth_year = birth_year
    
    #string representation
    def __str__(self):
        return f'{self.name} is a {self.breed} and was born in {self.birth_year}'
    
    # #human age
    def human_age(self):
        today = datetime.datetime.now()
        year = today.year
        return year - self.birth_year
       
    #write a method that will calculate dog years
    # def dog_years(self):
    #     # today = datetime.datetime.now()
    #     # year = today.year
    #     # return f'{self.name} is {year - self.birth_year} years old in dog years'
    def dog_years(self):
        return 7 * self.human_age()
    
dog1 = Dog('Fido', 'Poodle', 2021) #Created our first object of the dog class
dog2 = Dog('Lady', 'Terrier', 2019)
dog3 = Dog('Stella','Bulldog', 2018)

#string representation print out
# print(dog1) 
# print(dog2)
# print(dog3)

#human age print out
# print(dog1.human_age()) 
# print(dog2.human_age())
# print(dog3.human_age())

#dog Year Method
print(dog1.dog_years()) 
print(dog2.dog_years())
print(dog3.dog_years())

# today = datetime.datetime.now()
# year = today.year
# print(year)



# Create a point object with attributes x=2, y=3

# Let’s add a __str__ method to our Point2D class so we can print Point2D objects.


# Lets add __add__ to add objects of the same class together


# Lets try __sub__ to add objects of the same class together

# Let's try __eq__ method to test equality
'''What is the output of this code if we don't override ==?
What is the output if we override == to use value equality?
Is it the same or different? Why?

Without the __eq__ method, we will only be able to test if it is the same object
'''



# Let's try __lt__ method to test less than


# Setting with mutator methods



# Getting with accessor methods





''' Exercise - Date Class '''




 




'''
Exercise - Dog Class
'''






