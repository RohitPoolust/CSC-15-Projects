# hw6_2_PoolustR.py
# Uses exponenets to print certain numbers without .math
# Rohit Poolust
# 11.03.2021
# Lab 6

#Computes the power function without using .math
#Parameters: base value and exponent
#Returns the product if they were raised to the power
def intpower(x,k):
    product = 1
    if k > 0:
        for i in range(k):
            product*=x
    elif k == 0:
        product=1
    else:
        for i in range(-k):
            product*=(x)
        product = 1/product
    return product

def main():
    x=10
    for i in range(-5,6):
        print(i, intpower(x,i))
main()