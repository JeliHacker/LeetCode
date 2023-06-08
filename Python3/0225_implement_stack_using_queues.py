# https://leetcode.com/problems/implement-stack-using-queues/

import collections

class MyStack:
    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]
    
    def empty(self):
        return not len(self._queue)

    def toString(self):
        q = self._queue.copy()
        answer = []
        for i in range(len(q)):
            answer.append(q.popleft())
        print(answer)


myStack = MyStack()

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.toString()
myStack.pop()
myStack.toString()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
