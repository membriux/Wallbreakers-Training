'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
'''

import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = queue.Queue()



    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.put(x)
        size = self.q.qsize()
        while size > 1:
            self.q.put(self.q.get())
            size -= 1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.get()


    def top(self) -> int:
        """
        Get the top element.
        """
        temp = self.q.get()
        self.push(temp)
        return temp


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
