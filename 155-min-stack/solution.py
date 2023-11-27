class MinStack:
    def __init__(self):
        self.st = []
        self.min = []
    def push(self, val: int) -> None:
        self.st.append(val)
        if self.min:
           if self.min[-1]>=val: self.min.append(val)
        else:
            self.min.append(val)
    def pop(self) -> None:
        # print(self.st,self.min)
        p = self.st.pop()
        if self.min[-1]==p:
                self.min.pop()
    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()