import time

# Write a class named Car that has the following data attributes:

# - _ _year_model (for the car’s year model)
# - _ _make (for the make of the car)
# - _ _speed (for the car’s current speed)

# The Car class should have an _ _init_ _ method that accepts the car’s year model and make as arguments. 
# These values should be assigned to the object’s _ _year_model and _ _make data attributes. 
# It should also assign 0 to the _ _speed data attribute.

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

# The class should also have the following methods:

    # - accelerate()
    # The accelerate method should add 5 to the speed data attribute each time it is called.
    def accelerate(self):
        self.__speed += 5
        
    # - brake()
    # The brake method should subtract 5 from the speed data attribute each time it is called.
    def brake(self):
        self.__speed -= 5

    # - get_speed()
    # The get_speed method should return the current speed.
    def get_speed(self):
        return self.__speed 
    
    #if at acceleration, output the current speed with upward arrow    
    def up_speed(self):
        print(f"The {self.__year_model} {self.__make} current speed: {self.get_speed()} mph \U000021D1")
        time.sleep(1)
        
    #here provide an downward arrow to indicate the current speed is deceasing
    def down_speed(self):
        print(f"The {self.__year_model} {self.__make} current speed: {self.get_speed()} mph \U000021D3")
        time.sleep(1)
        
    #put a note that car engine shut off at 0 mph
    def car_stop(self):
        print(f"The {self.__year_model} {self.__make}  engine is shut off. \U0001F68F\U0001F696")