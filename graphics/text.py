from .base import Renderable


class TextBox(Renderable):
    def __init__(self, text = "No message given", x = 0, y = 0, w = 230, size = 2, rotation = 0, color = 'white', z = 0):
        super().__init__(x, y, z, color)
        self.text = text
        self.w, self.r = w, rotation
        self.size = size
    
    def draw(self, display):
        display.draw_text(self.text, self.x, self.y, self.w, self.size, self.r, self.c)