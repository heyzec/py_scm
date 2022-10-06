from py_scm.node import Node

class Col(Node):
    def add(self, *children):
        for child in children:
            self.add_child(child, 0, self.height)
        
    @property
    def width(self):
        widths = list(map(lambda child: child.width, self.children))
        if len(widths) == 0:
            return 0
        return max(widths)

    @property
    def height(self):
        return sum(map(lambda child: child.height, self.children))
