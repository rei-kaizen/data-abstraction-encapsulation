from FanProgram import Fan
# For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. 
# Assign medium speed, radius 5, color blue, and turn it off for the second object. 
# Display each object’s speed, radius, color, and on properties.

def TestFan():
    Eureka = Fan(1, True, 10, "yellow")
    print("EUREKA - Speed:", Eureka.get_speed(), "| Power On:",Eureka.get_on(), "| Radius:",Eureka.get_radius(), "| Color:",Eureka.get_color())

    Hanabishi = Fan(2, False, 5)
    print("HANABISHI - Speed:", Hanabishi.get_speed(), "| Power On:",Hanabishi.get_on(), "| Radius:",Hanabishi.get_radius(), "| Color:",Hanabishi.get_color())

TestFan()    