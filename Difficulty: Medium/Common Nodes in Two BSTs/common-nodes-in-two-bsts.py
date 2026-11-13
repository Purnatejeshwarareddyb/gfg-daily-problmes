''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        s1, s2 = set(), []
        def inorder1(node):
            if not node:
                return
            inorder1(node.left)
            s1.add(node.data)
            inorder1(node.right)

        def inorder2(node):
            if not node:
                return
            inorder2(node.left)
            if node.data in s1:
                s2.append(node.data)
            inorder2(node.right)

        inorder1(r1)
        inorder2(r2)
        return s2