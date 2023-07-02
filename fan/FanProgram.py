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
        if 1 > speed > 3:
            print("Invalid speed value. Speed should be 1(fast)/2(medium)/3(slow) 'v' ")
        else: 
            self.__speed = speed
        return self
        
    def get_on(self):
        return self.__on
    
    def set_on(self, on):
        if not isinstance(on, bool):
            print("This attribute's value is invalid. Boolean values (True/False) are needed here *_* .")
        else:    
            self.__on = on
        return self
    
    def get_radius(self):
        return self.__radius
    def set_radius(self, radius):
        if radius <= 0:
            print("Value for radius is invalid, it needs to be a positive number +.+")
        else:
            self.__radius = radius
        return self
           
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
        return self
    
    def properties(self):
        border_length = 40  # Length of the border
        fan_name = "Eureka Fan"  # Replace with the appropriate fan name

        #top border line
        top_border = "╔" + "═" * (border_length - 2) + "╗"

        #fan name line
        side_border1 = "║" + fan_name.center(border_length - 2) + "║"

        # Create the separator line
        separator = "╠" + "═" * (border_length - 2) + "╣"

        # Get the fan properties
        fan_deets1 = f"Speed: {self.get_speed()}  |  Power On: {self.get_on()}"
        fan_deets2 = f"Radius: {self.get_radius()}  |  Color: {self.get_color()}"
        side_border2 = "║" + fan_deets1.center(border_length - 2) + "║"
        side_border3 = "║" + fan_deets2.center(border_length - 2) + "║"

        # Create the bottom border line
        bottom_border = "╚" + "═" * (border_length - 2) + "╝"

        # Print the formatted output
        print(top_border)
        print(side_border1)
        print(separator)
        print(side_border2)
        print(side_border3)
        print(bottom_border)
