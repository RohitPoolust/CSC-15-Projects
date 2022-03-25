#File: hw4_1_PoolustR.py
#Program that outputs a die N times
# Rohit Poolust
# 10/20/2021
#LAB 4

import random
def main():
    #Input
    ntimes=int(input("Enter number of times die rolled:"))
    count=[0,0]
    for flips in range(ntimes):
        face=random.randint(1,6)
        #print(face)
        if face%2==0:
            count[0]+=1
        else:
            count[1]+=1
    #Output
    print(f'Odds: {count[1]}\nEven: {count[0]}')
main()