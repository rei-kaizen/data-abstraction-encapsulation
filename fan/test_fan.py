from fan_program import Fan
from output_format import Formatter
import pyfiglet

# For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. 
# Assign medium speed, radius 5, color blue, and turn it off for the second object. 
# Display each object’s speed, radius, color, and on properties.

def TestFan():
    formatter = Formatter()

    #1ST Object
    Eureka = Fan(1, True, 10, "yellow")
    print(pyfiglet.figlet_format("1ST", "small"))
    formatter.properties(Eureka)
    
    print()
    
    #2ND Object
    print(pyfiglet.figlet_format("2ND", "small"))
    Eureka.set_speed(1).set_on(False).set_radius(5).set_color("blue")
    formatter.properties(Eureka)
    
TestFan()
  