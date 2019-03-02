#Event loops

from microbit import *

while running_time() < 10000:
    display.show(Image.ANGERY)

display.show(Image.SAD)


from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.ANGRY)
    elif button_b.is_pressed():
        display.show(Image.HEART)

    else:
        display.show(Image.HAPPY)


display.clear()


