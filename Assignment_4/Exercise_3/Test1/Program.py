from Start import *
print "For the instructions press 'i'\n"


def Program():
    key = get()

    if key == 119:
        forward(5)
    elif key == 97:
        turn(-20)
    elif key == 100:
        turn(20)
    elif key == 115:
        forward(-5)
    elif key == 49:
        change_color_to("Black")
    elif key == 50:
        change_color_to("Red")
    elif key == 51:
        change_color_to("Blue")
    elif key == 52:
        change_color_to("Green")
    elif key == 105:
        instructions("W,A,S and D for movement.\n1,2,3 and 4 to change color.\nPress 'c' to clear all the lines")
    elif key == 99:
        clear()


run(Program)
from End import *
