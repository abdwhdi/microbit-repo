# this project is to print my name, haert, happy face
# tested on microbit v2 
# made from ABDWAHIDI
from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll('ABDWAHIDI')
        display.show(Image.HAPPY)
        sleep(1000)
        display.show(Image('00900:'
                           '09990:'
                           '99999:'
                           '09990:'
                           '00900'))