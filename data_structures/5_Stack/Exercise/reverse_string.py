#!/usr/bin/env python
# coding: utf-8

# In[32]:


from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


# In[33]:


s=Stack()
str="We will conquere COVID-19"
for i in str:
    s.push(i)
rev_str=''
while not s.is_empty():
    rev_str+=s.pop()
print(rev_str)

