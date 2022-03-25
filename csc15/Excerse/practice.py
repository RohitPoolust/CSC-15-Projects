def main():
    down_payment= float(input("What is the down payment:"))
    monthly_payment=float(input("what is the monthly payment:"))
    number_month=float(input("What are the # of months:"))

    total_cost= down_payment+monthly_payment*number_month
    print('The total cost would be:', total_cost)
main()


