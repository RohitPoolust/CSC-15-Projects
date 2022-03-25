# File hw5_functionsI.py
# Practice functions definition and testing using driver main()
# Name: Rohit Poolust
# Date: 10.27.2021

import math
import random

# Function Definitions ============================================

# -----------------------------------------------------------------
# Function to compute area of a circle
# Parameters: radius r
# Return: the are of the circle with radius r
def area_circle(r):
    area = math.pi*r**2
    return area

# -----------------------------------------------------------------
# Function radius_circle( area)
def radius_circle(a):
    r=math.sqrt(a/math.pi)
    return r
# -----------------------------------------------------------------
# Function word_count(text)
def word_count(text):
    list1=text.split()
    return len(list1)


# -----------------------------------------------------------------
# Function initialize_list0(n)
def initialize_list0(n):
    list=[]
    for i in range(1,n+1):
        list.append(0)
    return list


# -----------------------------------------------------------------
# Function initialize_list(n, value)
def initialize_list(n,value):
    list=[]
    for i in range(n):
        list.append(value)
    return list



# -----------------------------------------------------------------
# Function sum_rolls(n)
def sum_rolls(n):
    total=0
    for i in range(n):
        face1=random.randint(1,6)
        print(face1)
        total+=face1
    return f"n = {n} total is {total}"



# -----------------------------------------------------------------
# Function list_count(lst)
def list_count(lst):
    dic={'0':0 ,'+':0 ,'-':0 }
    #Finds if the numbers in list is -,0,+
    for i in range(len(lst)):
        if lst[i] > 0:
            dic['+']+=1
        elif lst[i] == 0:
            dic['0']+=1
        elif lst[i] < 0:
            dic['-']+=1
    return dic

# main() ----------------------------------------------------------
# Driver for testing the functions
def main():
    # 1. testing area_circle(r)
    print('*** Testing area_circle() ***')
    area=[]
    for r in range(1,6):
        print(f'r = {r},   area = {area_circle(r)}')
        area.append(area_circle(r))


    # 2. testing radius_circle(area)
    print('*** Testing radius_circle(area) ***')
    for m in area:
        print(f'area = {m}, r = {radius_circle(m)}')
    


    # 3. testing word_count(text)
    print('\n*** Testing word_count(text)***')
    text='We The People'
    #Asks user for output unitl they press enter
    while text != '':
        print(f'{text} has {word_count(text)} words')
        text=input()


    # 4. testing initialize_list0(n)
    print('\n*** Testing initialize_list0(n)***')
    #OUTPUT for initialize_list0(n)
    print(initialize_list0(1))
    print(initialize_list0(2))
    print(initialize_list0(3))
    print(initialize_list0(4))
    print(initialize_list0(5))


    # 5. testing initialize_list(n,value)
    print('\n*** Testing initialize_list(n, value)***')
    #OUTPUT for initializa_list(n,value)
    print(initialize_list(10,'*'))
    print(initialize_list(10,10))
    print(initialize_list(10,12.0))
    print(initialize_list(10,-1))


    # 6. testing sum_rolls(n)
    print('\n*** Testing num_rolls(n)***')
    #OUTPUT for sum_rolls(n)
    print(sum_rolls(-1))
    print(sum_rolls(0))
    print(sum_rolls(1))
    print(sum_rolls(5))
    
    # 7. testing list_count(lst)
    print('\n*** Testing list_count(lst) ***')
    #All types of lists possible
    list1= [0,1,0,-1,-2,3]
    list2=[0,0,0,0,0]
    list3=[1,2,3,4,5,6]
    list4=[-1,-2,-3,-4,-5]
    list5=[]

    #OUTPUT of function list_count(lst)
    print(list_count(list1))
    print(list_count(list2))
    print(list_count(list3))
    print(list_count(list4))
    print(list_count(list5))
    
    return
# end  of main()
 
main()    # call to main()

