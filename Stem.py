import turtle

# screen setup
wn = turtle.Screen()
wn.title("Thank you Mr.Hermanson")
wn.bgcolor("#111931")
t = turtle.Turtle()
t.color("black")
t.speed(0)

# Mr.Hermanson
t.penup()
t.goto(-100, 200)
t.pendown()
t.write("Thank you mr.Hermanson", font = ("Calibri" , 10, "bold") )
t.begin_fill()
t.color("yellow")
t.penup()
t.goto(-150, 230)
t.pendown()
for  i in range(2):
    t.fd(300)
    t.rt(90)
    t.fd(450)
    t.rt(90)
t.end_fill()
t.hideturtle()

turtle.done()