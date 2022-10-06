from __future__ import annotations
from typing import Optional
import abc

from py_scm.handler import Handler

class Node(abc.ABC):
    def __init__(self):
        self.children: list[Node] = []
        self.parent: Optional[Node] = None
        self.handlers: list[Handler] = []
        self.left = 0
        self.top = 0
        self._width = 0
        self._height = 0
        
    def add_child(self, child: Node, left, top):
        self.children.append(child)
        child.parent = self
        child.left = left
        child.top = top

    def draw(self, screen):
        for child in self.children:
            child.draw(screen)

    def attach(self, handler):
        self.handlers.append(handler)

    def handle(self, event, context):
        for handler in self.handlers:
            handler(event, context)

        for child in self.children:
            if not hasattr(event, 'pos') or child.contains(event.pos[0], event.pos[1]):
                child.handle(event, context)
    
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self, width):
        self._width = width

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def x(self):
        if self.parent is None:
            return 0
        return self.parent.x + self.left

    @property
    def y(self):
        if self.parent is None:
            return 0
        return self.parent.y + self.top

    def contains(self, x, y) -> bool:
        return (self.x <= x < self.x + self.width and self.y <= y < self.y + self.height)
