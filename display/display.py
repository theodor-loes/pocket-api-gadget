from picographics import PicoGraphics			# Universal graphics library - part of the uf2 file
from picographics import DISPLAY_PICO_DISPLAY_2	# Class for this model display
from picographics import PEN_P4
from pimoroni import Button						# Using buttons
from machine import lightsleep

import utime


class Display:
    def __init__(self):
        self.brightness = 1.0
        self.display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_P4, rotate=90)	# Horizontal orientation
        self.display.set_backlight(self.brightness)
        self.display.set_font("bitmap8")
        
        self.WIDTH, self.HEIGHT = self.display.get_bounds()
        self.__textSize = 2
        
        self.__penColors = {
            "WHITE": self.display.create_pen(255, 255, 255),
            "BLACK": self.display.create_pen(0, 0, 0),
            "RED"  : self.display.create_pen(178,34,34),
            "GREEN": self.display.create_pen(107,174,95),
            "BLUE" : self.display.create_pen(46,139,139),
            "YELLOW": self.display.create_pen(255,212,121),
            "BROWN": self.display.create_pen(139,108,66)
        }
        
        
        self.button_a = Button(12)
        self.button_b = Button(13)
        self.button_x = Button(14)
        self.button_y = Button(15)
        
        self.textboxes = []
    
    def clear(self):
        self._set_pen("BLUE")
        self.display.clear()
    
    def draw_text(self, text, x, y, x_limit, size, rotation, c):
        self._set_pen(c)
        self.display.text(text, x, y, x_limit, size, angle=rotation)
    
    def draw_line(self, x1, y1, x2, y2, thickness, c):
        self._set_pen(c)
        self.display.line(x1, y1, x2, y2, thickness)
    
    def draw_circle(self, x, y, r, c):
        self._set_pen(c)
        self.display.circle(x, y, r)
    
    def draw_polygon(self, points, c):
        self._set_pen(c)
        self.display.polygon(points)
    
    def update(self):
        self.display.update()
    
    def listen(self) -> str:
        keys = str()
        while True:
            if self.button_a.read():
                keys += 'A'
            if self.button_b.read():
                keys += 'B'
            if self.button_x.read():
                keys += 'X'
            if self.button_y.read():
                keys += 'Y'
            if keys:
                return keys
            
            utime.sleep(0.05)
    
    def _set_pen(self, color):
        self.display.set_pen(self.__penColors[color.upper()])