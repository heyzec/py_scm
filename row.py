from py_scm.node import Node

class Row(Node):
    def add(self, *children):
        for child in children:
            self.add_child(child, self.width, 0)
        
    @property
    def width(self):
        return sum(map(lambda child: child.width, self.children))
        
    @property
    def height(self):
        heights = list(map(lambda child: child.height, self.children))
        if len(heights) == 0:
            return 0
        return max(heights)
