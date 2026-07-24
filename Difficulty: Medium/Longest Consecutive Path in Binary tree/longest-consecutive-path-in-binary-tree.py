'''
Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def longestConsecutive(self, root):
        # code hear
        if not root:
            return -1
        
        self.max_len = 0
        
        def dfs(node, parent_val, current_len):
            if not node:
                return
            
            if parent_val is not None and node.data == parent_val + 1:
                current_len += 1
            else:
                current_len = 1
                
            self.max_len = max(self.max_len, current_len)
            
            dfs(node.left, node.data, current_len)
            dfs(node.right, node.data, current_len)
            
        dfs(root, None, 1)
        
        return self.max_len if self.max_len > 1 else -1

        