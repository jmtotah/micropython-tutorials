from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "freefall":
        display.show(Image.SURPRISED)
    else:
        display.show(Image.HAPPY)

from microbit import *
import random

answers = ["Leslie Totah", "Aubrey Totah", "Darius Totah" ]


while True:
    display.show("8")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))

    elif button_a.was_pressed():
         display.clear()
         sleep(1000)
         display.scroll("Jesse Totah")


