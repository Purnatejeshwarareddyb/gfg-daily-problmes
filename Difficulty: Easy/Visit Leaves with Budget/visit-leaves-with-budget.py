''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        # code here
        if not root:
            return 0

        q = [(root, 1)]
        leaves = []

        while q:
            node, level = q.pop(0)

            if not node.left and not node.right:
                leaves.append(level)
            else:
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))

        leaves.sort()

        count = 0
        for cost in leaves:
            if k >= cost:
                k -= cost
                count += 1
            else:
                break

        return count