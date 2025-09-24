class SceneManager:
    def __init__(self, display):
        self.display = display
        self.current_scene = None
    
    def set_scene(self, scene):
        self.current_scene = scene
    
    def render(self):
        if self.current_scene:
            self.display.clear()
            self.current_scene.draw(self.display)
        self.display.update()