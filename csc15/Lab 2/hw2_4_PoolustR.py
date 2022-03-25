#File: hw2_4_PoolustR.py
#Calculates the present value of prize 
# Rohit Poolust
# 09/22/2021
#LAB 2
import math
def main():
    print("Program calculates present value of monetary prize.")
#Inputs: Asks the user to input the name, amount, interest rate, and number years
    input_name = input("Winner:")
    input_amount= float(input("Enter prize amount in $:"))
    input_interest= float(input("interest rate in %:"))
    input_years= float(input("Enter number years:"))
#Calculates the present value and rounds
    present_value = (input_amount/math.pow((1+(input_interest/100)),input_years))
    present_value = round(present_value,2)
#Prints present value
    print(f"The present value of the prize for {input_name} after {input_years} years is {present_value}")
main()

