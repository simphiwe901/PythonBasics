# program which prompts the user's input and draws a desired shape
# turtle
# Simphiwe Mchunu
# 18 May 2015

import turtle

a = turtle.numinput("Petal Number", "Enter the number of petals (must be an even number): ")
b = turtle.numinput("Stem length", "Enter the stem length: ")
d = turtle.numinput("Side length", "Enter the length of side: ")
c = turtle.textinput("Petal type", "Enter the petal type (triangle, square, or pentagon): ")
e = turtle.textinput("Stem colour", "Enter the stem colour: ")
f = turtle.textinput("1st petal colour","Enter the first petal colour: ")
g = turtle.textinput("2nd petal colour", "Enter the second petal colour: ")
a = int(a)
k =360/a
r = 0
if a%2==0:
    turtle.speed(0)
    for i in range(a):
        if i%2==0:
            r +=k
            if c =="triangle":
                turtle.color(e)
                turtle.fd(b)
                turtle.color(f)
                turtle.left(30)
                turtle.fd(d)
                for i in range(2):
                    turtle.right(120)
                    turtle.fd(d)
                turtle.penup()
                turtle.home()
                turtle.pendown()
                turtle.right(r)
            elif c =="square":
                turtle.color(e)
                turtle.fd(b)
                turtle.color(f)
                turtle.right(45)
                turtle.fd(d)
                for p in range(3):
                    turtle.left(90)
                    turtle.fd(d)
                turtle.penup()
                turtle.home()
                turtle.pendown()
                turtle.right(r)
            elif c =="pentagon":
                turtle.color(e)
                turtle.fd(b)
                turtle.color(f)
                turtle.right(54)
                turtle.fd(d)
                for s in range(4):
                    turtle.left(72)
                    turtle.fd(d)
                turtle.penup()
                turtle.home()
                turtle.pendown()
                turtle.right(r)
        else:
            r +=k
            if c =="triangle":
                turtle.color(e)
                turtle.fd(b)
                turtle.color(g)
                turtle.left(30)
                turtle.fd(d)
                for n in range(2):
                    turtle.right(120)
                    turtle.fd(d)
                turtle.penup()
                turtle.home()
                turtle.pendown()
                turtle.right(r)
                turtle.color(e)
            elif c =="square":
                turtle.color(e)
                turtle.fd(b)
                turtle.color(g)
                turtle.right(45)
                turtle.fd(d)
                for m in range(3):
                    turtle.left(90)
                    turtle.fd(d)
                turtle.penup()
                turtle.home()
                turtle.pendown()
                turtle.right(r)
            elif c =="pentagon":
                turtle.color(e)
                turtle.fd(b)
                turtle.color(g)
                turtle.right(54)
                turtle.fd(d)
                for z in range(4):
                    turtle.left(72)
                    turtle.fd(d)
                turtle.home()
                turtle.pendown()
                turtle.right(r)

turtle.exitonclick()
