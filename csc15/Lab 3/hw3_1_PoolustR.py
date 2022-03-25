#File: hw3_1_PoolustR.py
# Asks user for type of ticket and prints the amount and price of tickets
# Rohit Poolust
# 09/29/2021
#LAB 3

def main():
#Prints the tickets
    print("Concert Tickets Master: make your selection!")
    print("For Orcestra, enter letters O or o.")
    print("For Tier 1, enter 1.")
    print("For Tier 2, enter 2.")
    print("For Balcony enter B or b.")
    print("Enter the letter q or Q if you want to quit anytime.")

    balcony_back=float(45.50)
    balcony_front=int(60.00)

    tier_two = int(150.00)
    tier_one = int(250.00)

    orch_front = int(95.00)
    orch_center = float(150.50)
    orch_back = int(80.00)
#Input: keyboard chooses sitting area
    sitting_area = input('Enter the sitting area choice:')
# If statment for orchestra 
    if sitting_area == 'O' or sitting_area == 'o':
        print("Enter F or f for orchestra front")
        print("Enter C or c for orchestra center")
        print("Enter B or b for orchestra back")
        orchestra_choice = input("Make your choice:")
        if orchestra_choice == 'F' or orchestra_choice == 'f':
            print("Price per ticket orchestra front is $95.00")
            num_tickets=int(input("How many tickets?"))
            price_tickets= num_tickets*orch_front
            print(f"{num_tickets} tickets at ochestra front cost ${price_tickets}")
        elif orchestra_choice == 'C' or orchestra_choice == 'c':
            print("Price per ticket orchestra front is $150.50")
            num_tickets=int(input("How many tickets?"))
            price_tickets= num_tickets*orch_center
            print(f"{num_tickets} tickets at ochestra center cost ${price_tickets}")
        elif orchestra_choice == 'B' or orchestra_choice == 'b':
            print("Price per ticket orchestra front is $80.00")
            num_tickets=int(input("How many tickets?"))
            price_tickets= num_tickets*orch_back
            print(f"{num_tickets} tickets at ochestra back cost ${price_tickets}")
        elif orchestra_choice == 'q' or orchestra_choice == 'Q':
            print("Goodbye!")
        else:
            print("Invalid Choice!")
# If statment for 'B' and 'b'
    elif sitting_area == 'B' or sitting_area == 'b':
        balcony_spot = input("Enter (bf) for balcony front or (bb) for balcony back:")
        if balcony_spot == "bf":
            print("Price per ticket balcony front is $60.00")
            num_tickets=int(input("How many tickets?"))
            price_tickets= num_tickets*balcony_front
            print(f"{num_tickets} tickets at balcony front cost ${price_tickets}")
        elif balcony_spot == 'bb':
            print("Price per ticket balcony back is $45.50")
            num_tickets=int(input("How many tickets?"))
            price_tickets= num_tickets*balcony_back
            print(f"{num_tickets} tickets at balcony back cost ${price_tickets}")
        elif balcony_spot == 'q' or balcony_spot == 'Q':
            print("Goodbye!")
        else:
            print("Invalid Choice!")
# If statement for '1'
    elif sitting_area == '1':
        print("Price per ticket tier two is $150.00")
        num_tickets=int(input("How many tickets?"))
        price_tickets= num_tickets*tier_two
        print(f"{num_tickets} tickets at tier two cost ${price_tickets}")
# If statement for '2'
    elif sitting_area == '2':
        print("Price per ticket tier one is $250.00")
        num_tickets=int(input("How many tickets?"))
        price_tickets= num_tickets*tier_one
        print(f"{num_tickets} tickets at tier one cost ${price_tickets}")
    elif sitting_area == 'q' or sitting_area == 'Q':
        print("Goodbye!")
    else:
        print('Invalid Choice!')
        return
main()
