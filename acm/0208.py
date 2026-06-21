from collections import defaultdict

class Trie(defaultdict):
    def __init__(self):
        super().__init__(Trie)
        self.end = False

    def insert(self, word):
        for w in word:
            self = self[w]
        self.end = True

    def search(self, word):
        for w in word:
            self = self.get(w)
            if self is None:
                return False
        return self.end

    def starts_with(self, word):
        for w in word:
            self = self.get(w)
            if self is None:
                return False
        return True