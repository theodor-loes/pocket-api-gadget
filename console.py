from picographics import PicoGraphics			# Universal graphics library - part of the uf2 file
from picographics import DISPLAY_PICO_DISPLAY_2	# Class for this model display
from picographics import PEN_P4
from pimoroni import Button						# Using buttons
from machine import lightsleep

import utime


class Textbox:
    def __init__(self, x = int(), y = int(), width = int(), height = int(), rotation = 0, display = None):
        self.position = (x, y)
        self.size = (width, height)
        self.rotation = rotation
        
        self.__screen = {
            "WIDTH": 240,
            "HEIGHT": 320
        }
        self.display = display
        self.__penColors = {
            "WHITE": self.display.create_pen(255, 255, 255),
            "BLACK": self.display.create_pen(0, 0, 0),
            "RED"  : self.display.create_pen(255, 000, 000),
            "GREEN": self.display.create_pen(000, 255, 000),
            "BLUE" : self.display.create_pen(000, 000, 255)
        }
    
    def write(self, text = str(), textSize: int = 2, color: str = "WHITE") -> None:
        self._clearScreen()
        self._setPen(color)
        self.display.text(text, self.position[0], self.position[1], self.position[0]+self.size[0], textSize, self.rotation)
        self.display.update()
    
    def _clearScreen(self) -> None:
        self._setPen("BLACK")
        self.display.clear()
    
    def _setPen(self, color: str) -> None:
        self.display.set_pen(self.__penColors[color])


class Display:
    def __init__(self):
        self.brightness = 1.0
        self.display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_P4, rotate=90)	# Horizontal orientation
        self.display.set_backlight(self.brightness)
        self.display.set_font("bitmap8")
        
        self.__screen = {
            "WIDTH": 240,
            "HEIGHT": 320
        }
        self.__textSize = 2
        
        self.__penColors = {
            "WHITE": self.display.create_pen(255, 255, 255),
            "BLACK": self.display.create_pen(0, 0, 0),
            "RED"  : self.display.create_pen(255, 000, 000),
            "GREEN": self.display.create_pen(000, 255, 000),
            "BLUE" : self.display.create_pen(000, 000, 255)
        }
        
        
        self.button_a = Button(12)
        self.button_b = Button(13)
        self.button_x = Button(14)
        self.button_y = Button(15)
        
        self.textboxes = []
    
    def Write(self, message = str(), color: str = "WHITE", x: int = 10, y: int = 10, width: int = 220, height: int = 310, rotation: int = 0) -> None:
        self.textboxes.append(Textbox(x, y, width, height, rotation, self.display))
        self.textboxes[-1].write(message, color = color)
    
    def ReadKey(self) -> str:
        while True:
            if self.button_a.read():
                return 'A'
            elif self.button_b.read():
                return 'B'
            elif self.button_x.read():
                return 'X'
            elif self.button_y.read():
                return 'Y'
            
            utime.sleep(0.05)
    
    def AwaitAwake(self) -> None:
        while True:
            if self.button_a.read():
                return 'A'
            elif self.button_b.read():
                return 'B'
            elif self.button_x.read():
                return 'X'
            elif self.button_y.read():
                return 'Y'
            
            lightsleep(2)
        
    def Cls(self) -> None:
        self.Empty()
        self.display.update()
    
    def Empty(self) -> None:
        self._setPen("BLACK")
        self.display.clear()
        self.__text = str()
    
    def TextReplace(self, substring, newSubstring) -> None:
        self.__text = self.__text.replace(str(substring), str(newSubstring))
    
    def Close(self) -> None:
        self.Cls()
        self.display.set_backlight(0.0)
    
    def SetBrightness(self, brightness: float) -> None:
        if brightness < 0:
            brightness = 0
        elif brightness > 1:
            brightness = 1
        self.display.set_backlight(brightness)
        self.brightness = brightness
    
    def _clearScreen(self) -> None:
        self._setPen("BLACK")
        self.display.clear()
    
    def _setPen(self, color: str) -> None:
        self.display.set_pen(self.__penColors[color])
    
    def _printText(self, color: str) -> None:
        self._clearScreen()
        self._setPen(color)
        self.display.text(self.__text, 10, 10, 236, self.__textSize)
        self.display.update()

