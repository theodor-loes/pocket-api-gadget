from .scene import Scene
from graphics import Circle
from graphics.assets import Tree, Cloud


class StartScene(Scene):
    def __init__(self, name):
        super().__init__(name)
        self.add(Tree(100, 50, 2))
        self.add(Tree(140, 140, 4))
        self.add(Tree(130, 30, 3))
        self.add(Tree(40, 57, 1))
        self.add(Cloud(2, 2, 3))
        self.add(Cloud(50, 30, 4))