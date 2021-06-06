class State:
    def __init__(self, num, lookup_table, child_count, is_root = False):
        self.num = num
        self.failure_link = None
        self._children = [None]*child_count
        self._root = is_root
        self._lookup_table = lookup_table
        self._children_list = []

    def add_child(self, edge, child):
        self._children[self._lookup_table[edge]] = child
        self._children_list.append(child)

    def get(self, c):
        c_id = self._lookup_table[c]
        if self._root:
            return self._children[c_id] or self
        return self._children[c_id]

    def get_no_lookup(self, c_id):
        if self._root:
            return self._children[c_id] or self
        return self._children[c_id]

    def get_link(self, c):
        c_id = self._lookup_table[c]
        return self._children[c_id]

    def get_children(self):
        return self._children_list

    def get_links(self):
        return [(c_id, child) for c_id, child in enumerate(self._children) if child is not None]
