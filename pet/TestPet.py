from PetProgram import Pet

# write a program that creates an object of the class and prompts  the user -
# to enter the name, type, and age of his or her pet. 
# This data should be stored as the object’s attributes. 
# Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.

#test

def TestPet():
    name = input("Pet name: ")
    type = input("Type: ")
    age = input("Age: ")

    pal = Pet(name, type, age)

    print(f"Pet Identification: {pal.get_name()}, {pal.get_animal_type()}, {pal.get_age()}")
    
TestPet()