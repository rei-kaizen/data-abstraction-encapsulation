from CarProgram import Car

# Next, design a program that creates a Car object then calls the accelerate method five times. 
# After each call to the accelerate method, get the current speed of the car and display it. 
# Then call the brake method five times. 

def TestCar():
    vroom = Car(1980, "Ford Capri 2.8i")

    for i in range(5):
        vroom.accelerate()
        print(f"The {vroom._Car__year_model} {vroom._Car__make} current speed: {vroom.get_speed} mph")

    for i in range(5):
        vroom.brake()
        print(f"The {vroom._Car__year_model} {vroom._Car__make} current speed: {vroom.get_speed()} mph")

TestCar()