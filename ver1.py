import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7789
import numpy as np
import JungDeaMan
import Joystick

JungDaeMan = JungDeaMan.JungDeaMan()
joystick = Joystick.Joystick()
my_image = Image.new("RGB", (joystick.width, joystick.height)) 
my_draw = ImageDraw.Draw(my_image)
my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
print("HElloo")

my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))

while True:
    command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
    
    if not joystick.button_U.value:  # up pressed
        command['up_pressed'] = True
        command['move'] = True

    if not joystick.button_D.value:  # down pressed
        command['down_pressed'] = True
        command['move'] = True

    if not joystick.button_L.value:  # left pressed
        command['left_pressed'] = True
        command['move'] = True

    if not joystick.button_R.value:  # right pressed
        command['right_pressed'] = True
        command['move'] = True

    JungDaeMan.move(command)

    #그리는 순서가 중요합니다. 배경을 먼저 깔고 위에 그림을 그리고 싶었는데 그림을 그려놓고 배경으로 덮는 결과로 될 수 있습니다.
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
    joystick.disp.image(my_image)