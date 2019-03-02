from microbit import *

while True:
    if pin2.is_touched():
        display.show(Image.CONFUSED)
    elif pin0.is_touched():
        display.show(Image.HAPPY)

    else:
        display.show(Image.ANGRY)
