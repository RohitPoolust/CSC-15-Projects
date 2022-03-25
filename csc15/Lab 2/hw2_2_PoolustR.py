#File: hw2_2_PoolustR.py
#Computes the mean Arithmetic, Geometric, and Harmonic
# Rohit Poolust
# 09/22/2021
#LAB 2
import math
def main():
    print("Calculate arithmetic, geometric and harmonic means of two numbers.")
    print("Enter two numbers which are not 0 and have the same sign")
#input: numbers that are not 0 and same sign
    number_1 = float(input('number 1:'))
    number_2 = float(input('number 2:'))
#Defines the harmonic gemetric and arithmetic mean
    harmonic_form = (2/((1/number_1)+(1/number_2)))
    geometric_form = math.sqrt(number_1*number_2)
    arithmetic_form = (number_1 + number_2)/2
#Output: Prints each mean
    print('Arithmetic mean is ', arithmetic_form)
    print('Geometric mean is ', geometric_form)
    print('Harmonic mean is: ', harmonic_form)
main()