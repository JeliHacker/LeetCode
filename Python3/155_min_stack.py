https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.length = 0
        
    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if len(self.minStack) > 0:
            self.minStack.append(min(self.minStack[self.length - 1], val))
        else:
            self.minStack.append(val)
        
        self.length += 1
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.length -= 1

    def top(self) -> int:
        
        return self.stack[self.length - 1]

    def getMin(self) -> int:
        answer = self.minStack[self.length - 1]
        return answer


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
