class MyStack:

    def __init__(self):
        self.main_stack = deque()
        self.stack_helper = deque()

    def push(self, x: int) -> None:
        self.stack_helper.append(x)
        while self.main_stack:
            self.stack_helper.append(self.main_stack.popleft())
        self.main_stack, self.stack_helper = self.stack_helper, self.main_stack
        
    def pop(self) -> int:
        return self.main_stack.popleft()
        
    def top(self) -> int:
        return self.main_stack[0]

    def empty(self) -> bool:
        return len(self.main_stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()