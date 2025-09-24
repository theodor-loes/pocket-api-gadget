from .base import Renderable


class Circle(Renderable):
    def __init__(self, x, y, r, color, z = 0):
        super().__init__(x, y, z, color)
        self.r = r
    
    def draw(self, display, offset = (0, 0)):
        ox, oy = offset
        display.draw_circle(self.x - ox, self.y - oy, self.r, self.c)


class Line(Renderable):
    def __init__(self, x, y, x1, y1, thickness, color, z = 0):
        super().__init__(x, y, z, color)
        self.x1, self.y1 = x1, y1
        self.t = thickness
    
    def draw(self, display, offset = (0, 0)):
        ox, oy = offset
        display.draw_line(self.x - ox, self.y - oy, self.x1 - ox, self.y1 - oy, self.t, self.c)
    

class Polygon(Renderable):
    def __init__(self, x, y, points: list, color, z = 0):
        super().__init__(x, y, z, color)
        self.points = [(x + point[0], y + point[1]) for point in points]
    
    def draw(self, display, offset = (0, 0)):
        ox, oy = offset
        points = [(point[0] - ox, point[1] - oy) for point in self.points]
        display.draw_polygon(points, self.c)


class Rectangle(Polygon):
    def __init__(self, x, y, w, h, color, z = 0):
        points = [(0, 0), (w, 0), (w, h), (0, h)]
        super().__init__(x, y, points, color, z)


class Triangle(Polygon):
    def __init__(self, x, y, x1, y1, x2, y2, color, z = 0):
        points = [(0, 0), (x1, y1), (x2, y2)]
        super().__init__(x, y, points, color, z)

