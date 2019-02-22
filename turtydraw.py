import turtle
t = turtle.Pen()
t.speed(100)


def left_spiral():
    global color_instruction
    global size_instruction
    for x in range(actual_size):
        t.forward(x)
        t.left(96)
def right_spiral():
    global color_instruction
    global size_instruction
    for x in range(actual_size):
        t.forward(x)
        t.left(94)
def thing_stuff():
    global color_instruction
    global size_instruction
    for x in range(actual_size):
        t.forward(x)
        t.left(209)
def cool_thing():
    global color_instruction
    global size_instruction
    for x in range(actual_size):
        t.forward(x)
        t.left(98)
while True:
    color_instruction = input("""What color do you want to draw?
                        5 green
                        6 blue
                        7 purple
                        8 yellow
                        9 red
                        10 pink""")
    if  color_instruction == "5":
        t.pencolor("green")
    if  color_instruction == "6":
        t.pencolor("blue")
    if  color_instruction == "7":
        t.pencolor("purple")
    if  color_instruction == "8":
        t.pencolor("yellow")
    if  color_instruction == "9":
        t.pencolor("red")
    if  color_instruction == "10":
        t.pencolor("pink")

    size_instruction = input("""What size do you want to draw your shape?
                        11 is 100
                        12 is 200
                        13 is 300
                        14 is 400
                        15 is 500
                        16 is 600""")
    if  size_instruction == "11":
        actual_size = 100
    if  size_instruction == "12":
        actual_size = int(200)
    if  size_instruction == "13":
        actual_size = int(300)
    if  size_instruction == "14":
        actual_size = int(400)
    if  size_instruction == "15":
        actual_size = int(500)
    if  size_instruction == "16":
        actual_size = int(600)

    shape_instruction = input("""What shape do you want to draw?
                        1 left spiral,
                        2 right spiral
                        3 design
                        4 design2 """)
    if  shape_instruction == "1":
        left_spiral()
    if  shape_instruction == "2":
        right_spiral()
    if  shape_instruction == "3":
        thing_stuff()
    if  shape_instruction == "4":
        cool_thing()
