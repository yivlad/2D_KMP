from .state import State


class Automaton:
    def __init__(self):
        self._root = None
        self.state = None
        self._v = 1
        self._lookup_table = []
        self._children_count = 0

    def reset(self):
        self.state = self._root

    def _get_new_state(self):
        state = State(self._v, self._lookup_table, self._children_count)
        self._v += 1
        return state

    def build(self, words):
        self.load_lookup_table(words)
        self._root = State(0, self._lookup_table, self._children_count, True)
        self._root.failure_link = self._root
        self.state = self._root
        word_states = []
        for word in words:
            state = self._root
            for c in word:
                if state.get_link(c) is None:
                    state.add_child(c, self._get_new_state())
                state = state.get_link(c)
            word_states.append(state.num)

        queue = []
        for child in self._root.get_children():
            child.failure_link = self._root
            queue.append(child)
        while len(queue) > 0:
            state = queue.pop(0)
            for c_id, child in state.get_links():
                failure = state.failure_link
                while failure.get_no_lookup(c_id) is None:
                    failure = failure.failure_link
                child.failure_link = failure.get_no_lookup(c_id)
                queue.append(child)

        return word_states

    def go(self, c):
        while self.state.get(c) is None:
            self.state = self.state.failure_link
        self.state = self.state.get(c)

    def load_lookup_table(self, words):
        letters = set([letter for word in words for letter in word])
        self._lookup_table = [0]*(max(letters)+1)
        i = 0
        for letter in letters:
            self._lookup_table[letter] = i
            i = i+1
        self._children_count = len(letters)
