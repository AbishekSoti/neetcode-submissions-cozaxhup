class MyHashSet:

    def __init__(self):
        self.list_of_values = [[] for i in range(1001)]


    def add(self, key: int) -> None:

        if key not in self.list_of_values[key%1000]:
            self.list_of_values[key%1000].append(key)

    def remove(self, key: int) -> None:
        if key in self.list_of_values[key%1000]:
            self.list_of_values[key%1000].remove(key)


    def contains(self, key: int) -> bool:
        if key in self.list_of_values[key%1000]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)