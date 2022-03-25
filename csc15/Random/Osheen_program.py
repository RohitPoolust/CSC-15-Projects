def date():
    x = input("Would you like to go out with me tomorrow?(Type (yes) or (no)): ")
    while x != 'yes':
        print("Sorry wrong answer! Try Again!")
        x = input("Maybe choose the other answer. Would you like to go out with me tomorrow?(Type (yes) or (no)): ")
    if x == 'yes':
        print('Very good choice, see you tmr!')


def main():
   date()
main()
#def max(lst):
#    temp=lst[0]
#    for i in range(len(lst)):
#        if lst[i] > temp:
#            temp=lst[i]
#    return i

#def main():
#    list1=[1,3,4,5,6,900,1000,700,100000000]
#    print(max(list1))
#main()
