# https://realpython.com/beginners-guide-python-turtle/

import turtle

s = turtle.getscreen()

t = turtle.Turtle()

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

u = input("Press enter to continue")
t.clear()
t.circle(50)


u = input("Press enter to continue")
t.clear()
t.goto(100,100)
t.circle(60)



u = input("Press enter to continue")
t.clear()
t.home()

u = input("Press enter to continue")
t.clear()
t.dot(20)

u = input("Press enter to continue")
t.clear()
turtle.bgcolor("blue")

u = input("Press enter to continue")
t.clear()
t.fillcolor("red")

u = input("Press enter to continue")
t.pencolor("green")

u = input("Press enter to continue")
t.clear()
t.shape("turtle")

u = input("Press enter to continue")
t.clear()
t.penup()
t.forward(100)
t.right(90)
t.pendown()
t.stamp()

u = input("Press enter to continue")
t.clear()


u = input("Would you like me to draw a shape? Type yes or no: ")
if u == "yes":
    t.circle(50)