import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7789
import numpy as np
import Joystick

class JungDeaMan:
    def __init__(self, width, height) :
        # 정대만이 가져야하는 변수들
        # 팔각도, 외형, 시작점

        # 팔각도는 0 ~ 90도
        self.shoulderAngel = 45
        self.power = 0
        # 힘은 
        self.position = np.array([0, 0, 0, 0])


    def move(self, command = None) :
        # 상, 하 -> 팔 각도 변경
        if command['up_pressed']:
            if (self.shoulderAngel != 90) : self.shoulderAngel += 5
    
        
        if command['down_pressed']:
            if (self.shoulderAngel != 0) : self.shoulderAngel -= 5