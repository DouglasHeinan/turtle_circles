from turtle import Turtle, Screen
import random


def main():
    # makes a spirograph.
    gap = int(input("How many degrees should Thomas shift between circles? (Smaller numbers make more circles.) "))
    screen = Screen()
    thomas = Turtle()
    screen.colormode(255)
    thomas.speed("fastest")
    for i in range(360 // gap):
        color = choose_color()
        thomas.pencolor(color)
        thomas.circle(100)
        thomas.left(gap)
    screen.exitonclick()


def choose_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


if __name__ == "__main__":
    main()

# turtle program for drawing a random walk pattern, changing direction and color of path randomly before each segment.
#     screen = Screen()
#     thomas = Turtle()
#     screen.colormode(255)
#     thomas.pensize(10)
#     thomas.hideturtle()
#     thomas.speed(10)
#     facing = [0, 90, 180, 270]
#     thomas.forward(10)
#
#     for i in range(100):
#         thomas.pencolor(choose_color())
#         thomas.setheading(random.choice(facing))
#         thomas.forward(25)
#
#     screen.exitonclick()
#
#
# def choose_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


