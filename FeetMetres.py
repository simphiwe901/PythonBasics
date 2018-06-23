# a program that displays a conversion table for measurements in feet to measurements in metres.
# Simphiwe Mchunu
#11 May 2015
import math

def main():
    minimum=int(input("Enter the minimum number of feet (not less than 0):\n"))
    maximum=int(input("Enter the maximum number of feet (not more than 99):\n"))
    for i in range(minimum,maximum+1):
        print(" {0:>3}' |   {1:<4.2f}m".format(i,i/3.2808) )
main()
