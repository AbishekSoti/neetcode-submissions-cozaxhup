class MyHashMap:

    def __init__(self):
        self.hash_map = [[] for x in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key% 1000 # Index means bucket index/which bucket the index is referring to, not its internal values.
            
        for kv_pair in self.hash_map[index]:
            if key == kv_pair[0] and value != kv_pair[1]:
                kv_pair[1] = value
                return
        #if [key,value] not in self.hash_map[index]:
        self.hash_map[index].append([key,value])
            

    def get(self, key: int) -> int:
        index = key% 1000
        for kv_pair in self.hash_map[index]:
            if key == kv_pair[0]:
                return kv_pair[1]

        return -1


    def remove(self, key: int) -> None:
        index = key%1000     
        for i,kv_pair in enumerate(self.hash_map[index]):
            if key == kv_pair[0]:
                self.hash_map[index].pop(i)
                return


# hash_map = [[] for x in range(1000)]
# index = 5%1000
# hash_map[index].append([5,2])
# print(hash_map[index])
# print(hash_map[4])
# print(len(hash_map[4]))
# hash_map[index].append([5,7])
# print(hash_map[index])

# hash_map[5%1000].remove([5,7])
# print(len(hash_map))
# print(len(hash_map[5%1000]))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)