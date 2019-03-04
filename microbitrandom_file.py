from microbit import *
import random

names = ["Hershey", "Zachary", "Leslie", "Aubrey", "Philip", "Darius", "Jesse" ]

display.scroll(random.choice(names))

from microbit import *
import random

display.show(str(random.randint(1, 6)))

from microbit import *
import random

display.show(str(random.randrange(0, 10)))


from microbit import *
import random

random.seed(8)
while True:
    if button_a.was_pressed():
        display.show(str(random.randrange(0, 10)))

        from microbit import *
import random

names = ["Hershey", "Zachary", "Leslie", "Aubrey", "Philip", "Darius", "Jesse" ]

random.seed(1000)
while True:
    if button_a.was_pressed():
        display.scroll(random.choice(names))

