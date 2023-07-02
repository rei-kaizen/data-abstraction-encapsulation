from CarProgram import Car

# Next, design a program that creates a Car object then calls the accelerate method five times. 
# After each call to the accelerate method, get the current speed of the car and display it. 
# Then call the brake method five times. 

def TestCar():
    vroom = Car(1980, "Ford Capri 2.8i")
    
    #call the methods in order
    
    vroom.red_light()
    vroom.yellow_light()
    vroom.green_light()
    vroom.car_sfx()
    vroom.roadway()

    for i in range(5):
        vroom.accelerate()
        vroom.up_speed()

    for i in range(5):
        vroom.brake()
        vroom.down_speed()
    
    vroom.car_stop()    
    vroom.roadway()
    
TestCar()