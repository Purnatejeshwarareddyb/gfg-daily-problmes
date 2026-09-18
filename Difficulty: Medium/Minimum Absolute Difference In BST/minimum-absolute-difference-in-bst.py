'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
        # code here
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.data - self.prev)
            self.prev = node.data

            inorder(node.right)

        inorder(root)
        return self.min_diff