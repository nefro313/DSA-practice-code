class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size+=1
    def pop(self):
        if self.is_empty():
            IndexError("Stack is empty")
            return
        poped_node = self.head
        self.head = self.head.next
        self._size-=1
        return poped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.data

    def size(self):
        return self._size
    def is_empty(self):
        return self.head is None

stack = LinkedListStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(9)
print(stack.pop())  # Output: 2
print(stack.peek())  
print(stack.size())