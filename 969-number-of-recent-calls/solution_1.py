# https://leetcode.com/problems/number-of-recent-calls
# https://leetcode.com/problems/969-number-of-recent-calls
class RecentCounter:

    def __init__(self):
        self.queue = []
        self.pointer = -1

    def ping(self, t: int) -> int:
        self.queue = [t]+self.queue
        self.pointer += 1
        for i in range(self.pointer,-1,-1):
            if self.queue[i]>=t-3000:
                self.pointer = i
                return i+1

        return len(self.queue) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)