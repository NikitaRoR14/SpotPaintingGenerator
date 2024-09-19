import turtle
import random
import colorgram

colors = colorgram.extract('painting.jpg',25)
def transfer_colors(colors):
    rgb_colors = []
    for color in colors:
        rgb = color.rgb
        r = rgb.r
        g = rgb.g
        b = rgb.b
        rgb_colors.append((r,g,b))
    return rgb_colors

def print_dot():
    turtle.dot(20, random.choice(color_list))


def update_position(indent):
    turtle.pu()
    turtle.goto(-250,-200 + (50*indent))

screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(15)
position = turtle.position()

color_list = transfer_colors(colors)

for row in range(0,10):
    update_position(row)
    for _ in range(10):
        print_dot()
        turtle.pu()
        turtle.forward(50)
        turtle.pd()
        print_dot()

screen.exitonclick()

