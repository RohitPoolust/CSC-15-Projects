#File: hw4_2_PoolustR.py
#Rolls two dice and finds sum if 6 or 7
# Rohit Poolust
# 10/20/2021
#LAB 4
import random
def main():
    CONSTANT1=6
    CONSTANT2=7
    #Input
    ntimes=int(input("Enter number of times 2 dice are rolled:"))
    count=0
    for flips in range(ntimes):
        face1=random.randint(1,6)
        face2=random.randint(1,6)
        #print(face1,face2)
        if face1+face2==CONSTANT1 or face1+face2==CONSTANT2:
            count+=1
    #Output
    print('Number of successes (sum is in [6,7]) is', count)
main()
