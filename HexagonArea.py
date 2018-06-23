# calculates the area of an hexagon
# Given the length of the side by user
# simphiwe mchunu
# 21 april 2015

def main():
   length = eval(input("Enter the lenghth of the side (cm):\n"))
   conversion = 3*3**0.5
   Area = (conversion/2)*length**2
   print("The area of a hexagon of side", length,"is {0:5.3f}".format(Area), end= ".")
main()
