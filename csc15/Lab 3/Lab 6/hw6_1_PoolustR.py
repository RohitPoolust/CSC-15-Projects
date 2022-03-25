# File hw6_1.Rpoolust.py
# Create function for the golden ratio
# Name: Rohit Poolust
# Date: 11.03.2021
#Lab #6


def goldenRatio():
    goldenratio= (1 + 5**(1/2))/2
    return goldenratio

def goldenRatioInfo():
    print("Phi can be defined by taking a stick and breaking it into two portions. If the ratio between these two portions is the same as the ratio between the overall stick and the larger segment, the portions are said to be in the golden ratio. This number is much similar to e and pi irrational numbers.")
    return
def goldenRatioFormula():
    print('(1 + 5^(1/2))/2')
    return

def main():
    print(goldenRatio())
    goldenRatioInfo()
    goldenRatioFormula()
main()

