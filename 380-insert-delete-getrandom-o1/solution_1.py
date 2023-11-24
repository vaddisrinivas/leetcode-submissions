# https://leetcode.com/problems/insert-delete-getrandom-o1
# https://leetcode.com/problems/380-insert-delete-getrandom-o1
class RandomizedSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val in self.s: return False
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.s: return False
        self.s.remove(val)
        return True
        
    def getRandom(self) -> int:
        return random.choice(list(self.s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()