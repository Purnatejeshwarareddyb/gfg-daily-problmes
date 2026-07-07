'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        

class Solution:
    def sumBT(self, root):
        # code hear
        if not root:
            return 0
        return root.data + self.sumBT(root.left) + self.sumBT(root.right)