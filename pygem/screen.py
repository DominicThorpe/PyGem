import pygame

class GemScreen:
    _instance = None
    
    
    def __new__(self):
        if self._instance is None:
            self._instance = super(GemScreen, self).__new__(self)
        
        return self._instance
