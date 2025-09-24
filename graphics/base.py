class Renderable:
    def __init__(self, x, y, z, color = 'white'):
        # z - render order
        self.x, self.y, self.z = x, y, z
        self.c = color
    
    def draw(self, display, offset = (0, 0)):
        raise NotImplementedError