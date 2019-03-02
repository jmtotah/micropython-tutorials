from microbit import *
display.show(Image.HAPPY)

from microbit import *
display.show(Image.SURPRISED)

from microbit import *
display.show(Image.CONFUSED)

#DIY Images
from microbit import *

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")

display.show(boat)

from microbit import *

house = Image("00700:07070:77777:700007:79007:79007")

display.show(house)

#Animation
from microbit import *

display.show(Image.ALL_ARROWS, loop=True, delay=300)

#Explodingdiamond
from microbit import *

diamond1 = Image("00000:00000:00300:00000:00000:")

diamond2 = Image("00000:00500:05050:00500:00000:")

diamond3 = Image("00700:07070:70007:07070:00700:")

diamond4 = Image("90009:00000:00000:00000:90009:")

diamond5 = Image("00900:00900:99999:00900:00900:")

diamond6 = Image("00000:00000:00000:00000:00000:")

diamond7 = Image("00900:00900:99999:00900:00900:")

all_diamonds = [diamond1, diamond2, diamond3, diamond4, diamond5, diamond6, diamond7]
display.show(all_diamonds, loop=True, delay=400)
