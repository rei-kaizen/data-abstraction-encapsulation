# Write a class named Pet, which should have the following data attributes:

# - _ _name (for the name of a pet)
# - _ _animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
# - _ _age (for the pet’s age)
# The Pet class should have an _ _init_ _ method that creates these attributes. 

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
# It should also have the following methods:

# - set_name()
# This method assigns a value to the _ _name field.
    def set_name(self, name):
        self.__name = name

# - get_name()
# This method returns the value of the _ _ name field.
    def get_name(self):
        return self.__name

# - set_animal_type()
# This method assigns a value to the _ _animal_type field.
    def set_animal_type(self, animal_type):
        if animal_type.isnumeric():
            print("I made the same mistake, and trust me, it makes me question my reading skills, so spare yourself the blunder and preserve your sanity.")
        else:
            self.__animal_type = animal_type

# - get_animal_type()
# This method returns the value of the _ _animal_type field.
    def get_animal_type(self):
        return self.__animal_type   
 
# - set_age()
# This method assigns a value to the _ _age field.
    def set_age(self, age):
        if age <= 0:
            print("Yeah age is just a number but it can't be negative ~~")
        else:
            self.__age = age
            
# - get_age()
# This method returns the value of the _ _age field.   
    def get_age(self):
        return self.__age