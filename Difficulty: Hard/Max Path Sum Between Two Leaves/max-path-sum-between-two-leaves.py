'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def solve(node):
            if not node:
                return float('-inf')

            if not node.left and not node.right:
                return node.data

            left = solve(node.left)
            right = solve(node.right)

            if node.left and node.right:
                self.max_sum = max(self.max_sum, left + right + node.data)
                return max(left, right) + node.data

            return (left if node.left else right) + node.data

        val = solve(root)

        if self.max_sum != float('-inf'):
            return self.max_sum

        return -1
        