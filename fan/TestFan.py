from FanProgram import Fan

# For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. 
# Assign medium speed, radius 5, color blue, and turn it off for the second object. 
# Display each object’s speed, radius, color, and on properties.

def TestFan():
    Eureka = Fan(1, True, 10, "yellow")
    print("Fan 1:")
    Eureka.properties()
    print()
    print("Fan 2:")
    Eureka.set_speed(1).set_on(False).set_radius(5).set_color("blue").properties()
    
TestFan()    