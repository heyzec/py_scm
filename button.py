import pygame
from py_scm.handler import Handler

from py_scm.node import Node

class Button(Node):
    attached = []

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.width = 50
        self.height = 50
        
        # self.attach(Handler(lambda x, y: print("CLciked"), pygame.MOUSEBUTTONDOWN))
        
    # @property
    # def width(self):
    #     return self._width

    # @property
    # def height(self):
    #     return self._height

    def draw(self, screen):
        img = pygame.font.SysFont(None, 24).render(self.text, True, '#FFFFFF')
        screen.blit(img, (self.x, self.y))
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, "#FFFFFF", rect, 2)
        
