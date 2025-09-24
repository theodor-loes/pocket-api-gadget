from graphics.assets import StickFigure
from graphics import Rectangle, Line
from graphics import TextBox


class Scene:
    def __init__(self, name):
        self.name = name
        self.objects = []
        self.static_objects = []
        
        self.bottom_bar()
        self.stick_figure()
        
        self.camera_x = 0
        self.camera_y = 0
    
    def add(self, obj, static = False):
        if static:
            self.static_objects.append(obj)
            self.static_objects.sort(key=lambda o: o.z)
        else:
            self.objects.append(obj)
            self.objects.sort(key=lambda o: o.x)

    def bottom_bar(self):
        self.add(Rectangle(0, 320-30, 240, 30, 'BROWN', z = 4), True)
        self.add(TextBox("14:12", 10, 320-21, 40, 2, 0, 'white', z = 5), True)
        self.add(TextBox("24. sep", 240-80, 320-21, 80, 2, 0, 'white', z = 5), True)
        self.add(Line(0, 320-30, 240, 320-30, 2, 'white', z = 4), True)
    
    def stick_figure(self):
        self.add(StickFigure(240 // 2, round(320 * 0.65), scale = 0.7, z = 0, color = 'white'), True)
    
    def draw(self, display):
        for obj in self.objects:
            obj.draw(display, offset = (self.camera_x, self.camera_y))
        for obj in self.static_objects:
            obj.draw(display)
    
    def move_camera(self, dx, dy):
        self.camera_x += dx
        self.camera_y += dy