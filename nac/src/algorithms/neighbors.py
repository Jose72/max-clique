
class Neighbors:

    def __init__(self):

        self.N = []

    def add(self, k, node):

        self.N.append((k, node))

    def get_n_n(self):
        if len(self.N):
            return self.N.pop()
        return 0, None



