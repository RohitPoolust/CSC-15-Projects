#File: hw1_4_Rohit Poolust.py
#Program that outputs Average rain fall
# Rohit Poolust
# 09/15/2021
#LAB 1

def main():
    #input total amount of rain and the number of days it rained
    total_rain_fall= int(input("What is the total rain fall?"))
    number_days= int(input("How many days did it rain?"))

    #finds the average rain fall 
    average_rain_fall=float(total_rain_fall/number_days)
   
    #prints the rounded average rainfall 
    print("The average rain fall is:", end ='')
    print('{:.2f}'.format(average_rain_fall))
main()