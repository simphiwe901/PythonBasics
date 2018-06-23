# program which prompts the user to enter the information about their credit card
#displays the formatted output
# simphiwe mchunu
# 21 april 2015

def main():
    a = input("Enter the card holder's name:\n")
    b = input("Enter the 16 digit card number (no spaces please):\n")
    c = input("Enter the date of issue (mm:yy):\n")
    d = input("Enter the expiry date (mm:yy):\n")
    e = input("Enter the 3 digit security code:\n")
    f = int(input("Enter the credit limit (Rand):\n"))
    g = int(input("Enter the balance (Rand):\n"))
    name = " Credit Card Account "
    avl = f - g
    h_1 = b[0:4]
    h_2 = b[4:8]
    h_3 = b[8:12]
    h_4 = b[12:16]
    i_1 = c[0:2]
    i_2 = c[3:5]
    j_1 = d[0:2]
    j_2 = d[3:5]
    sp = ""
    r = "Rand"
    print("+""{0:-^47}".format(name)+"+")
    print("| Card holder:""{0:^22}".format(a),"{0:>11}".format(sp)+"|")
    print("| Card number:""{0:^25}".format(h_1+" " +h_2+" "+h_3+" "+ h_4),"{0:>8}".format(sp)+"|")
    print("| Date of issue:""{0:^7}".format(i_1+"/"+i_2),"  " "Expiry date:", j_1+"/"+j_2,"{0:>3}".format(sp)+"|")
    print("| Security code:""{0:^5}".format(e),"{0:>26}".format(sp)+"|")
    print("| Credit limit:""{0:^12.2f}".format(f),"{0:>20}".format(sp)+"|")
    print("| Availabe:""{0:^20.2f}".format(avl),"{0:>16}".format(sp)+"|")
    print("| Balance:""{0:^21.2f}".format(g),"{0:>16}".format(sp)+"|")
    print("+""{0:-^47}".format(sp)+"+")

main()
