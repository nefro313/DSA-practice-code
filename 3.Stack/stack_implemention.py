
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        if self.is_empty():
            return IndexError("Stack is empty")
        return len(self.items)

stack = Stack()
# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.size())  # Output: 1
print(stack.is_empty())  # Output: False
print(stack.pop())  # Output: 1
print(stack.is_empty())  