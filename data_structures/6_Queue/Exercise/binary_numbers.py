#!/usr/bin/env python
# coding: utf-8

# In[10]:


from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def last(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.buffer[-1]


# In[15]:


binary_queue=Queue()
i=0
binary_queue.enqueue('1')
while i<10:
    f=binary_queue.last()
    binary_queue.enqueue(f+'0')
    binary_queue.enqueue(f+'1')
    print(binary_queue.dequeue())
    i+=1


# In[ ]:




