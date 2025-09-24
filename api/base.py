from .api import Api


class Base(Api):
    def __init__(self, display):
        self.display = display
    
    def execute(self):
        raise NoImplementedError("Must implement execute method")