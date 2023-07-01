# (The Fan class)
# Design a class named Fan to represent a fan. The class contains:
# Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
# A private int data field named speed that specifies the speed of the fan.
# A private bool data field named on that specifies whether the fan is on (the default is False).
# A private float data field named radius that specifies the radius of the fan.
# A private string data field named color that specifies the color of the fan.
# A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).


    def __init__(self, speed = 1, on = False, radius = 5,  color = "blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
        
# The accessor(getters) and mutator(setters) methods for all four data fields.
    
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed
        
    def get_on(self):
        return self.__on
    def set_on(self, on):
        self.__on = on
        
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        self.__radius = radius
        
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

# # For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. 
# # Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each object’s speed, radius, color, and on properties.

# Eureka = Fan(1, True, 10, "yellow")
# print("EUREKA - Speed:", Eureka.get_speed(), "| Power:",Eureka.get_on(), " | Radius:",Eureka.get_radius(), "| Color:",Eureka.get_color())

# Cooler = Fan(2, False, 5)
# print("COOLER - Speed:", Cooler.get_speed(), "| Power:",Cooler.get_on(), "| Radius:",Cooler.get_radius(), " | Color:",Cooler.get_color())