#I=In, O=Out. Also did movment in the y and x axis
from microbit import *

while True:
    reading = accelerometer.get_z()
    if reading > 20:
        display.show("I")
    elif reading < -20:
        display.show("O")
    else:
        display.show("-")

from microbit import *
import music

while True:
    music.pitch(abs(accelerometer.get_y()*10), 10)
