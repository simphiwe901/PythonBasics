# program which prompts the user's input and calculates the amount of tax applicable
# Based on their earnings
# Simphiwe Mchunu
# 03 April 2015

def tax():
    a = int(input("Enter your earnings per annum(per year):\n"))
    b = input("Enter the type of organisation you work for:\n")
    if a < 36000 or b == "Charity":
        print("You don't get taxed at all")
        print("Your net earnings are", "R"+str(a) + ".00" )
    elif 36000 < a < 720000 and b =="Government":
        c = (a*15)/100
        c_1 = a - c
        print("You get taxed","R"+ c,"of your salary")
        print("Your net earnings are","R"+c_1)
    elif 36000 < a < 72000 and b == "Company":
        d = (a*20)/100
        d_1 = a - d
        print("You get taxed","R"+str(d)+".00","of your salary")
        print("Your net earnings are","R"+str(d_1)+".00")
    else:
        e = (a*25)/100
        e_1 = a - e
        print("You get taxed","R"+str(e)+".00", "of your salary")
        print("Your net earnings are","R"+str(e_1)+".00")

tax()
