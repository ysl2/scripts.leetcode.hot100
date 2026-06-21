from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        print(self)
        return self[key]

    def put(self, key, val):
        self[key] = val
        self.move_to_end(key)
        if len(self) > self.capacity:
            self.popitem(last=False)
        print(self)

lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))
lru_cache.put(3, 3)
print(lru_cache.get(2))
lru_cache.put(4, 4)
print(lru_cache.get(1))
print(lru_cache.get(3))
print(lru_cache.get(4))