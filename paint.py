# program which calculates the number of cans needed to paint a wall
# Value calculated according to the Area
# Simphiwe Mchunu
# 10 May 2015

def main():
    a = input("Enter length: ")
    b = input ("Enter height: ")
    if a.isnumeric and b.isnumeric:
        Area = int(a)*int(b)
        c = Area//5
        d = (Area//5) + 1
        if Area%5==0:
            print("Area is",Area,"and requires",c,"cans")
        elif Area == 5:
            print("Area is",Area, "and requires",c,"can")
        else:
            print("Area is",Area, "and requires",d,"cans")
    else:
        print("Error: Invalid input")
main()
