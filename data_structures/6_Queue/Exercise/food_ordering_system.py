#!/usr/bin/env python
# coding: utf-8

# In[7]:


from collections import deque
import threading
import time
class Order:
    
    def __init__(self):
        self.buffer = deque()
    
    def place_order(self, val):
        for i in val:
            self.buffer.appendleft(i)
            print("Ordered", i)
            time.sleep(0.5)
        
    def serve_order(self):
        while True:
            time.sleep(2)
            if len(self.buffer)==0:
                print("Queue is empty")
                return
            print("Served", self.buffer.pop())
        

    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
orders = ['pizza','samosa','pasta','biryani','burger']
t=time.time()
pq=Order()
t1=threading.Thread(target=pq.place_order, args=(orders,))
t2=threading.Thread(target=pq.serve_order)

t1.start()
t2.start()

