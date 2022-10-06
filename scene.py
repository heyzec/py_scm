import abc
from py_scm.node import Node

class Scene(Node):
    # def __init__(self):
        # self.objects: list[PlacedObject] = []

    def on_setup(self):
        pass

    def on_draw(self, screen):
        self.draw(screen)
        # for placed in self.objects:
        #     obj = placed.node
        #     x, y = placed.x, placed.y
        #     obj.draw(screen, x, y)

    @property
    def x(self):
        return 0

    @property
    def y(self):
        return 0

    def on_event(self, event, context):
        super().handle(event, context)

    def place(self, node: Node, x: float, y: float):
        self.add_child(node, x, y)
