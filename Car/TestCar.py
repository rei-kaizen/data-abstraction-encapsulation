from CarProgram import Car
import time

# Next, design a program that creates a Car object then calls the accelerate method five times. 
# After each call to the accelerate method, get the current speed of the car and display it. 
# Then call the brake method five times. 

def TestCar():
    vroom = Car(1980, "Ford Capri 2.8i")
    
    #red light
    print("-" * 12)
    print("| \U0001F534 \U000026AB \U000026AB |  \033[31mREADY!\033[0m")
    print("-" * 12)
    time.sleep(2)
    
    #yellow light
    print("-" * 12)
    print("| \U000026AB \U0001F7E1 \U000026AB |  \033[93mSET!\033[0m")
    print("-" * 12)
    time.sleep(2)
   
    #green light
    print("-" * 12)
    print("| \U000026AB \U000026AB \U0001F7E2 |  \033[32mGO!\033[0m")
    print("-" * 12)
    time.sleep(2)
    
    print()    
    print("vrooom vrooomm .... " * 2 + " \U0001F695 \U0001F4A8")
    time.sleep(2)
    
    #road string
    print("\033[90m" + ("-" * 17 + "|")*2 + "-" * 17 + "\033[0m")

    for i in range(5):
        vroom.accelerate()
        print(f"The {vroom._Car__year_model} {vroom._Car__make} current speed: {vroom.get_speed()} mph")
        time.sleep(1)

    for i in range(5):
        vroom.brake()
        print(f"The {vroom._Car__year_model} {vroom._Car__make} current speed: {vroom.get_speed()} mph")
        time.sleep(1)
    
    print(f"The {vroom._Car__year_model} {vroom._Car__make} engine is shut off. \U0001F68F\U0001F696")
    
    #road string
    print("\033[90m" + ("-" * 17 + "|")*2 + "-" * 17 + "\033[0m")
    
TestCar()