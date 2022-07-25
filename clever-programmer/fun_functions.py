import turtle

my_turtle = turtle.Turtle()
wn = turtle.Screen()
def square(a, b):
    my_turtle.forward(a)
    my_turtle.left(b)
    my_turtle.forward(a)
    my_turtle.left(b)
    my_turtle.forward(a)
    my_turtle.left(b)
    my_turtle.forward(a)

# square(100, 90)
# square(200, 90)
# square(23, 45)
wn.exitonclick()
