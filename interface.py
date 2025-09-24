from console import Display
from options import Hue, Yr, Time
from machine import deepsleep
from pimoroni import RGBLED
import utime


class Interface(Display):
    def __init__(self):
        super().__init__()
        
        self.Close()
        RGBLED(6, 7, 8).set_rgb(0, 0, 0)
        self.AwaitAwake()
        self.SetBrightness(1)
        
        self.hue = Hue(self)
        self.yr = Yr(self)
        self.time = Time(self)
        
    def HomeMenu(self):
        self.WriteLine("Choose what file to run")
        self.WriteLine("To scroll, press Y and B\nTo select, press X\nTo turn off/on, press A")
        self.Write("D:\programs> ")
        options = ["PhilipsHue.py", "GetWeather.py", "GetCurrentTime.py", "Flashlight.py", "Settings.py"]	# MUST BE IN SAME ORDER AS self.__supportedFeatures
        response = self.Scroll(options)
        
        self.WriteLine()
        self.WriteLine("\nSelected")
        utime.sleep(0.5)
        actions = [self.hue.execute, self.yr.execute, self.time.execute, self.Flashlight, self.Settings]
        actions[response]()
    
    def Scroll(self, options: list) -> int:	# Returns index of chosen option
        i, j = 0, 0			# Where j is the previous i
        self.Write(options[i])
        while True:
            button = self.ReadKey()
            if button == 'X':
                return i
            elif button == 'A':
                deepsleep(1)
            else:
                if button == 'Y':
                    i = i-1 if i != 0 else i			# Scroll back
                elif button == 'B':
                    i = i+1 if i != len(options)-1 else i	# Scroll forward
                    
                # Update on screen
                self.TextReplace(options[j], options[i])
                self.Write()
                j = i
    
    def Settings(self):
        self.Empty()
        self.WriteLine("Change screen-brightness")
        self.WriteLine("-------------------------")
        self.WriteLine("Adjust with Y and B")
        self.WriteLine("Save with X or A")
        
        self.ChangeBrightness()
    
    def Flashlight(self):
        self.Empty()
        self._setPen("WHITE")
        self.display.clear()
        self.display.update()
        
        self.ChangeBrightness()
    
    def ChangeBrightness(self):
        while True:
            button = self.ReadKey()
            if button == "Y" and self.brightness < 1.0:
                self.brightness += 0.1
                self.SetBrightness(self.brightness)
            elif button == "B" and self.brightness > 0.0:
                self.brightness -= 0.1
                self.SetBrightness(self.brightness)
            elif button in ["A", "X"]:
                return None
        
        
        