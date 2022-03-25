#File: hw4_3_PoolustR.py
#Creates histogram from users input on sum of dice rolled
#Rohit Poolust
#10/20/2021
#LAB 4
import random
def main():
    #Input
    ntimes1=int(input('Enter the number of rolls:'))
    hist={2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:'',11:'',12:''}

    #Keeps rolling dice for ntimes1
    for i in range(ntimes1):
        face1=random.randint(1,6)
        face2=random.randint(1,6)
        sumface=face1+face2
        #print(sumface)
        hist[sumface]+='*'
    #Output    
    for j in range(2,13):
            print(j,hist[j])
    return
main()
    