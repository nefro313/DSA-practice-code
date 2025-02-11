class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_element(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while(curr_node.next):
            curr_node = curr_node.next
        curr_node.next = new_node
        self.tail = curr_node.next
        
    def travase(self):
        if  self.head is None:
            print("list is empty")
            return
        curr_node = self.head
        while(curr_node):
            print(curr_node.data,curr_node.next)
            curr_node = curr_node.next

    def serach_element(self,data):
        if  self.head is None:
            print("list is empty")
            return
        curr_node = self.head
        while(curr_node):
            if curr_node.data == data:
                return True
            curr_node = curr_node.next
            
    def delete(self,data):
        if  self.head is None:
            print("list is empty")
            return
        if  self.head.data == data:
            self.head = self.head.next
            return
        curr_node = self.head
        while(curr_node.next.data != data):
            curr_node = curr_node.next
        if self.tail.data == data:
            curr_node.next = None
            return
        curr_node.next = curr_node.next.next
    
    def dlt_prev_element(self,data):
        if  self.head is None:
            print("list is empty")
            return
        curr_node = self.head
        if self.head.next.data == data:
            print("here too")
            self.head=  None
            self.head = curr_node.next
            return
        prev = None
        while curr_node and curr_node.data != data:
            before_prev = prev
            prev = curr_node
            curr_node = curr_node.next
        if curr_node and prev:
            if before_prev:
                before_prev.next = curr_node
                
    def revese_list(self):
        if  self.head is None:
            print("list is empty")
            return
        curr_node = self.head
        prev = None
        while(curr_node):
            next_node = curr_node.next
            curr_node.next = prev
            prev  = curr_node
            curr_node = next_node
        self.head = prev
    def middle_element(self):
        if  self.head is None:
            print("list is empty")
            return
        slow = self.head
        fast = self.head
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
            
        
_list = LinkedList()
_list.add_element(50)
_list.add_element(60)
_list.add_element(90)
_list.add_element(80)
_list.add_element(500)
# _list.delete(500)
# _list.dlt_prev_element(90)
# _list.revese_list()
_list.middle_element()
_list.travase()