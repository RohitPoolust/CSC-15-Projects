#File: hw2_1_PoolustR.py
#Program that outputs total profit
# Rohit Poolust
# 09/22/2021
#LAB 2

def main():
#Constants 
    BLOCK_PRICE = 52900.00
    COST_UNIT_ECECTROC = 0.12
    HWR_DEPRICIATION = 100.00

# INPUT: num of block mined and units of electricity 
    print("Program calculates profit of a bitcoin miner.")
    num_block_mined = float(input("How many blocks?"))
    num_units_elec = float(input("How many hours?"))

#OUTPUT: net monthly profit for the miner
    total_block_mined = BLOCK_PRICE * num_block_mined
    total_units_elec = COST_UNIT_ECECTROC * num_units_elec
# Prints the Net Monthly Profit
    TOTAL_PROFIT = total_block_mined - (HWR_DEPRICIATION + total_units_elec)
    print('$',TOTAL_PROFIT)

main()