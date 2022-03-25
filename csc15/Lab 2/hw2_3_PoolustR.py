#File: hw2_3_PoolustR.py
# Prints name and Phone number of user
# Rohit Poolust
# 09/22/2021
#LAB 2

def main():
    print("Program to print personal data.")
#Input: Obtains users name and number
    user_name = input("Enter name:")
    user_number = int(input("Enter 10-digit integer number:"))
#Output: Finds section of phone number
    first_three = user_number//10000000
    middle_three = ((user_number % 10000000)//10000)
    last_four = user_number % 10000

#Combines phone number and prints
    phone_number = f"({first_three}){middle_three}-{last_four}"
    print(user_name, phone_number)
main()