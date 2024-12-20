#!/usr/bin/env python
# coding: utf-8

# In[11]:


class TreeNode:
    def __init__(self, data1, data2):
        self.name = data1
        self.designation=data2
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, val):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if val=="both":
            print(prefix + self.name + '(' + self.designation + ')')
        elif val=="name":
            print(prefix + self.name)
        elif val=="designation":
            print(prefix + self.designation)
        if self.children:
            for child in self.children:
                child.print_tree(val)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")


# In[ ]:




