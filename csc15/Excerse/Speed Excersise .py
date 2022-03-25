def main():
    # named constants
    flying_speed= 500.0
    driving_speed= 60.0
    #get input from keyboard
    distance=float(input('What is the distance: '))#Assigns distanace in float
    #get travel time
    time_fly=distance/flying_speed
    time_drive=distance/driving_speed

    print('Flying will take:', time_fly)
    print('Driving will take:', time_drive)
    

main()
