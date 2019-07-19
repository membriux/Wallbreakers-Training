class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}

    def get(self, key: int) -> int:
        try:
            val = self.d[key]
        except:
            return -1

        del self.d[key]
        self.d[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
        self.d[key] = value

        if self.cap < len(self.d):
            del self.d[next(iter(self.d))]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
