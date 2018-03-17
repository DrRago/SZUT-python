import turtle
def drawLine(s, howOften):
    if howOften == 0:
        turtle.forward(s)
    else:
        drawLine(s/3, howOften - 1)
        turtle.left(60)
        drawLine(s/3, howOften - 1)
        turtle.right(120)
        drawLine(s/3, howOften - 1)
        turtle.left(60)
        drawLine(s/3, howOften - 1)

def eck(size, zeit, ecken):
    winkel = 360 / ecken
    for i in range(ecken):
        drawLine(size, zeit)
        turtle.right(winkel)

if __name__ == "__main__":
    turtle.title("Python ist suppppppppaaaaaaaaaaaaaaahhhhhhhhhhhh")
    turtle.ht()
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-300, 200)
    turtle.pendown()
    eck(1, 0, 500)
    turtle.done()