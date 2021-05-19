class State:
    def __init__(self, num, is_root = False):
        self.num = num
        self.failure_link = None
        self._children = {}
        self._root = is_root

    def add_child(self, edge, child):
        self._children[edge] = child

    def get(self, c):
        if c in self._children:
            return self._children[c]
        if self._root:
            return self
        return None

    def get_link(self, c):
        if c in self._children:
            return self._children[c]
        return None

    def get_children(self):
        return self._children.values()

    def get_links(self):
        return self._children.items()
