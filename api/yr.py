from .base import Base


class Yr(Base):
    def __init__(self, display):
        super().__init__(display)
        self.url = "https://weatherforecast-pico.theodor-tobiassen.workers.dev/"
    
    def execute(self):
        response = self.request(method='GET', url = self.url, timeout = 10)
        
            