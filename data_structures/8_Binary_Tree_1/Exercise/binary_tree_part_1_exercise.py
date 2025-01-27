#!/usr/bin/env python
# coding: utf-8

# In[20]:


class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
                
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)
            
    def in_order_traversal(self):
        elements=[]

        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        
        return elements
    
    def find_min(self):
        if not self.left:
            return self.data
        else:
            return self.left.find_min()
    def find_max(self):
        if not self.right:
            return self.data
        else:
            return self.right.find_max()
    def calculate_sum(self):
        sum_total=0
        if self.left:
            sum_total+=self.left.calculate_sum()
        sum_total+=self.data
        if self.right:
            sum_total+=self.right.calculate_sum()
        return sum_total
            
    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    
    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements
        
    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        
    
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root  
        
if __name__=='__main__':
    numbers=[17,4,1,20, 9, 23,18,34,18,4]
    numbers = [15,12,7,14,27,20,23,88 ]

    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())

