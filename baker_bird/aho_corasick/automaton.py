from .state import State


class Automaton:
    def __init__(self):
        self._root = State(0, True)
        self._root.failure_link = self._root
        self._v = 1
        self.state = self._root

    def reset(self):
        self.state = self._root

    def _get_new_state(self):
        state = State(self._v)
        self._v += 1
        return state

    def build(self, words):
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
            for c, child in state.get_links():
                failure = state.failure_link
                while failure.get(c) is None:
                    failure = failure.failure_link
                child.failure_link = failure.get(c)
                queue.append(child)

        return word_states

    def go(self, c):
        while self.state.get(c) is None:
            self.state = self.state.failure_link
        self.state = self.state.get(c)
