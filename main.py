import turtle

# --- Setup (steps 2-4) ---
ts = turtle.getscreen()
ts.setup(700, 600)
ts.bgcolor("lightsteelblue")
t = turtle.Turtle()
t.speed(0)
t.pensize(3)


# --- Helper functions ---
def go(x, y):
    """Move without drawing, then face right."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()


def disc(x, y, r, fill, outline="black"):
    """Filled circle centered on (x, y)."""
    go(x, y - r)
    t.color(outline, fill)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def rect(x, y, w, h, fill, outline="black"):
    """Filled rectangle with bottom-left corner at (x, y)."""
    go(x, y)
    t.color(outline, fill)
    t.begin_fill()
    for side in (w, h, w, h):
        t.fd(side)
        t.lt(90)
    t.end_fill()


# --- Ground ---
rect(-350, -300, 700, 100, "seagreen", "darkgreen")

# --- Moon ---
disc(-250, 230, 40, "lightyellow", "goldenrod")

# --- Body, belly, feet ---
disc(0, -120, 80, "sienna")
disc(0, -125, 45, "tan")
disc(-40, -200, 20, "sienna")
disc(40, -200, 20, "sienna")
disc(-40, -203, 9, "tan")
disc(40, -203, 9, "tan")

# --- Arms (thick lines) ---
t.color("sienna")
t.pensize(10)
go(-75, -90)
t.setheading(150)
t.fd(60)
go(75, -90)
t.setheading(30)
t.fd(60)
t.pensize(3)

# --- Ears (drawn before the head) ---
disc(-75, 115, 28, "sienna")
disc(75, 115, 28, "sienna")
disc(-75, 115, 14, "tan")
disc(75, 115, 14, "tan")

# --- Head and muzzle ---
disc(0, 40, 90, "sienna")
disc(0, 15, 40, "tan")

# --- Eyes ---
disc(-30, 65, 14, "white")
disc(30, 65, 14, "white")
disc(-30, 65, 6, "royalblue")
disc(30, 65, 6, "royalblue")

# --- Cheeks and nose ---
disc(-62, 30, 10, "salmon", "salmon")
disc(62, 30, 10, "salmon", "salmon")
disc(0, 30, 9, "black")

# --- Smile (arc) ---
go(-22, 8)
t.color("black")
t.setheading(-60)
t.circle(25, 120)

# --- Top hat ---
rect(-55, 125, 110, 12, "black", "black")      # brim
rect(-38, 137, 76, 60, "black", "black")       # crown
rect(-38, 137, 76, 12, "crimson", "crimson")   # hat band

# --- Bow tie ---
t.color("royalblue", "royalblue")
go(0, -48)
t.begin_fill()
t.goto(-30, -33)
t.goto(-30, -63)
t.goto(0, -48)
t.end_fill()
t.begin_fill()
t.goto(30, -33)
t.goto(30, -63)
t.goto(0, -48)
t.end_fill()
disc(0, -48, 6, "navy", "navy")

# --- Caption ---
go(0, -275)
t.color("white")
t.write("Hi, I'm Freddy Bear!", align="center", font=("Arial", 16, "bold"))

# --- Finish: send the turtle home without drawing ---
t.penup()
t.home()
t.hideturtle()

# Optional commands from the lab to try:
# t.undo()    -> undo the last action
# t.clear()   -> erase the turtle's drawings
# t.reset()   -> clear everything and reset to defaults

turtle.done()
