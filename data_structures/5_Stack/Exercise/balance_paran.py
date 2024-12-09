#!/usr/bin/env python
# coding: utf-8

# In[93]:


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
    
    def is_balanced(self, str):
        for i in str:
            if i in "({[":
                self.push(i)
            if i==')':
                if not self.is_empty() and self.pop()=='(':
                    #self.pop()
                    continue
                else:
                    return False
            if i=='}':
                if not self.is_empty() and self.pop()=='{':
                    #self.pop()
                    continue
                else:
                    return False
            if i==']':
                if not self.is_empty() and self.pop()=='[':
                    #self.pop()
                    continue
                else:
                    return False
            
            
        return self.is_empty()
            


# In[94]:


s=Stack()
s.is_balanced("({a+b})")


# In[95]:


s.is_balanced("))((a+b}{")


# In[96]:


s.is_balanced("((a+b))")


# In[97]:


s.is_balanced("))")


# In[99]:


s.is_balanced("[a+b]*(x+2y)*{gg+kk}")


# In[ ]:




