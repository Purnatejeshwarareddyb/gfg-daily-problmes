''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        # code here
        self.ans = float('-inf')

        def dfs(node):
            if not node:
                return float('inf')

            if not node.left and not node.right:
                return node.data

            left_min = dfs(node.left)
            right_min = dfs(node.right)

            min_descendant = min(left_min, right_min)
            self.ans = max(self.ans, node.data - min_descendant)

            return min(node.data, min_descendant)

        dfs(root)
        return self.ans