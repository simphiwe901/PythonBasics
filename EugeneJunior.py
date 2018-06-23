# prompts the user
# predict the user's star war
# simphiwe mchunu
# 21 april 2015

def main():
    print("Hello, I am Eugene Junior.")
    name = input("What is your first name?\n")
    surname = input("What is your last name?\n")
    a = name[0:1]
    b = surname[0:1]
    print("Hi",a+"."+b, end= ".!\n")
    year =eval(input("What year is this?\n"))
    age = eval(input("what age are you?\n"))
    birth_year = year - age
    birth_year2 = year - age + 1
    x = birth_year2[-2:]
    print("Okay, so you were born in", int(birth_year)+ "/"+ int(x),end= ".")
    height = input("How tall are you (metres) ?\n")
main()
