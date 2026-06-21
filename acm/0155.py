class MinStack(list):
    def __init__(self):
        super().__init__()

    def push(self, val):
        self.append((val, val if not self else min(self[-1][1], val)))

    def top(self):
        return self[-1][0]

    def get_min(self):
        return self[-1][1]