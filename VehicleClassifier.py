# a program that determines the class to which a vehicle belongs.
# Based on the Gross Vehicle Mass (GVM)
# simphiwe Mchunu
# 11 May 2015

def main():
    print("***** Vehicle classifier *****")

    GVM=eval(input("What is the gross vehicle mass (in kg)?\n"))
    trailer=input("Does the vehicle have a trailer?\n")

    if trailer=="y":
        gvm=eval(input("What is gross vehicle mass of the trailer (in kg)?\n"))

        if gvm<=750 and GVM<=3500:
            print("This vehicle is class B.")
        elif gvm>750 and GVM<=3500:
            print("This vehicle is class EB.")
        elif gvm>750 and 16000>=GVM>3500:
            print("This vehicle is class EC1.")
        elif gvm>750 and GVM>16000:
            print("This vehicle is class EC.")
        elif gvm<=750 and 16000>=GVM>3500:
            print("This vehicle is class C1.")
        elif gvm<=750 and GVM>16000:
            print("This vehicle is class C.")
    elif trailer=="n":

        articulated=input("Is the vehicle articulated?\n")
        if articulated=="n" and articulated=="n" and GVM<=3500:
            print("This vehicle is class B.")
        elif articulated=="n" and articulated=="n" and 16000>=GVM>3500:
            print("This vehicle is class C1.")
        elif articulated=="n" and articulated=="n" and GVM>16000:
            print("This vehicle is class C.")

        elif GVM<=3500 and articulated=="y":
            print("This vehicle is class EB.")
        elif 16000>=GVM>3500 and articulated=="y":
            print("This vehicle is class EC1.")
        elif GVM>16000 and articulated=="y":
            print("This vehicle is class EC.")
main()
