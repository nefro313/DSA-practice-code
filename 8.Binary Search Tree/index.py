class BST:
    def __init__(self,key):
        self.key = key
        self.l_child = None
        self.r_child = None
        
    def insert(self,data):
        
        if self.key is None:
            self.key = data
            return
        
        if self.key == data:
            return
        
        if data < self.key:
            if self.l_child:
                self.l_child.insert(data)
            else:
                self.l_child = BST(data)
        else:
            if self.r_child:
                self.r_child.insert(data)
            else:
                self.r_child = BST(data)
        
    def search(self,data):
        if self.key is None:
            print("The tree is empty")
            return 
        if self.key == data:
            print("Node is Founded")
            return True
        if data < self.key:
            if self.l_child:
                self.l_child.search(data)
            else:
                print("Not founded")
        else:
            if self.r_child:
                self.r_child.search(data)
            else:
                 print("Not founded")
                 
    def pre_order_travesel(self):
        if self.key is None:
            return
        print(self.key)
        if self.l_child:
            self.l_child.pre_order_travesel()
        if self.r_child:
            self.r_child.pre_order_travesel()
    def inorder_travesel(self):
        if self.key is None:
            return
        if self.l_child:
            self.l_child.inorder_travesel()
        print(self.key)
        if self.r_child:
            self.r_child.inorder_travesel()
            
    def delete(self,data):
        if self.key is None:
            print("The tree is empty")
            return 
        if data < self.key:
            if self.l_child:
                self.l_child = self.l_child.delete(data)
            else:
                print("The Node is not Presents in this tree")
        elif data > self.key:
            if self.r_child:
                self.r_child = self.r_child.delete(data)
            else:
                print("The Node is not Present in this tree")
        else:
            if self.l_child is None:
                temp = self.r_child
                self = None
                return temp
            if self.r_child is None:
                temp = self.l_child
                self = None
                return temp
            node = self.l_child
            while node.r_child:
                node = node.r_child
            self.key = node.key
            self.l_child = self.l_child.delete(node.key)
        return self
root = BST(None)

root.insert(50)
root.insert(10)
root.insert(60)
root.insert(5)
root.insert(30)
root.insert(90)

print(root.key)
print(root.l_child.key)
print(root.r_child.key)
# print(root.search(6))
root.delete(90)
print(root.pre_order_travesel())