import  microbit

import os

with open('hello.txt', 'w') as my_file:
    my_file.write("How's it going?")

microbit.display.scroll(os.listdir()[0])



import  microbit

import os

with open('hello.txt', 'w') as my_file:
    my_file.write("How's it going?")

with open('hello.txt') as my_file:
    microbit.display.scroll(my_file.read())



