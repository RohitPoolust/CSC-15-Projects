#File: hw4_4_PoolustR.py
#Compares two dice and returns the greater value if possible
#Rohit Poolust
#10/20/2021
#LAB 4

import random
def main():
    list=[]
    total=0
    succ_rolls=0

    old_face=0
    new_face=0

    while new_face>=old_face:
        old_face=new_face

        rolls=random.randint(1,6)
        list.append(rolls)
        
        total+=new_face
        succ_rolls+=1

        new_face=rolls

    succ_rolls-=1

    #OUTPUT
    print(f'All rolled faces: {list}')
    print(f'Total of sucessful rolls: {total}')
    print(f'Number of sucessful rolls: {succ_rolls}')

main()



