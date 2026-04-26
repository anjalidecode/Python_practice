import turtle

# create window
wn = turtle.Screen()
wn.setup(500, 500)
wn.title("Pattern Drawing")

# create turtle
alex = turtle.Turtle()
alex.shape("turtle")
alex.speed(1)   # fastest drawing

# colors for pattern
colors = ["red", "green", "blue"]

# draw pattern
for color in colors:
    alex.color(color)
    for i in range(1, 6):
        alex.circle(20 * i)
    alex.left(120)

# keep window open
wn.mainloop()