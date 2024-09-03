class MyHashSet:

    def __init__(self):

        self.set = {}
        

    def add(self, key: int) -> None:

        self.set[key] = 1
        

    def remove(self, key: int) -> None:

        self.set[key] = 0
        

    def contains(self, key: int) -> bool:
        if key in self.set and self.set[key] == 1:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)