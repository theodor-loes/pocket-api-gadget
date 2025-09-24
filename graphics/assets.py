from .shapes import *
from random import randint


class StickFigure(Renderable):
    def __init__(self, x, y, scale = 1.0, thickness = 2, color = 'white', z = 0):
        super().__init__(x, y, z, color)
        self.scale = scale
        self.thickness = thickness
        self.color = color

        head_radius = round(13 * scale)
        body_length = round(60 * scale)
        arm_length = round(20 * scale)
        leg_length = round(10 * scale)

        # dictionary of body parts
        self.body = {
            # Head (outline effect: big circle, then smaller inside)
            "head_outer": Circle(x, y - body_length // 2 - head_radius,
                                 head_radius, color),
            "head_inner": Circle(x, y - body_length // 2 - head_radius,
                                 head_radius - self.thickness, "black"),

            # Body
            "torso": Line(x, y - body_length // 2,
                          x, y + body_length // 5 * 2,
                          thickness, color),

            # Arms
            "arm_left": Line(x, y - body_length // 3,
                             x - arm_length, y + body_length // 6,
                             thickness, color),
            "arm_right": Line(x, y - body_length // 3,
                              x + arm_length, y + body_length // 6,
                              thickness, color),

            # Legs
            "leg_left": Line(x, y + body_length // 4,
                             x - leg_length, y + body_length,
                             thickness, color),
            "leg_right": Line(x, y + body_length // 4,
                              x + leg_length, y + body_length,
                              thickness, color),
        }
    
    def draw(self, display):
        for part in self.body.values():
            part.draw(display)
    
    def move(self, dx, dy):
        """Shift the entire stickman by (dx, dy)."""
        self.x += dx
        self.y += dy
        for part in self.body.values():
            part.move(dx, dy)



class Tree(Renderable):
    def __init__(self, x, y, size=1, z=0):
        super().__init__(x, y, z)
        self.size = size

        self.stem_width = 5 * size
        self.stem_height = (14 + randint(0, 6)) * size

        # Generate leaves properly relative to the top of the stem
        self._leaves = self._create_leaves(size)

        # Body = stem + leaves
        self.body = [Line(x, y, x, y - self.stem_height, self.stem_width, 'brown')]
        for leaf in self._leaves:
            self.body.append(
                Circle(x + leaf[0], y - self.stem_height + leaf[1], leaf[2], 'green')
            )

    def _create_leaves(self, size):
        layers = 2
        leaves_per_layer = 3
        leaves = []

        # Each layer is above the stem with small vertical offset
        layer_spacing = 8 * size  # vertical spacing between layers
        max_horizontal_spread = 10 * size  # how far leaves can go sideways

        for i in range(layers):
            y_offset = i * layer_spacing  # from top of stem
            for j in range(leaves_per_layer):
                # spread leaves evenly, then add slight random shift
                x_offset = ((j - leaves_per_layer // 2) * 6 + randint(-2, 2)) * size
                radius = randint(3, 7) * size
                leaves.append((x_offset, -y_offset, radius))  # negative y because up
        return leaves

    def draw(self, display, offset=(0, 0)):
        for item in self.body:
            item.draw(display, offset)


class Cloud(Renderable):
    def __init__(self, x, y, size = 1, color = 'white', z = 1):
        super().__init__(x, y, z)
        self.size = size
        
        r = size*2*randint(2, 3)
        self.parts = [
            Circle(x, y, r, color = color),
            Circle(x - r, y + randint(0, r//3), r*10//randint(12, 20), color = color),
            Circle(x + r, y + randint(0, r//2), r*10//randint(12, 20), color = color)
        ]
    
    def draw(self, display, offset=(0, 0)):
        for part in self.parts:
            part.draw(display, offset)