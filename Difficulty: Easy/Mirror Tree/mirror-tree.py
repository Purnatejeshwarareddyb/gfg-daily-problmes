'''
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def mirror(self, root):
        #code hear
        if not root:
            return

        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)