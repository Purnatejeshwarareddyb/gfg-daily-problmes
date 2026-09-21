"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""


class Solution:

    def areAnagrams(self, root1, root2):
        """ code here """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        q1 = [root1]
        q2 = [root2]

        while q1 and q2:
            n1 = len(q1)
            n2 = len(q2)

            if n1 != n2:
                return False

            level1 = []
            level2 = []

            next_q1 = []
            next_q2 = []

            for node in q1:
                level1.append(node.data)
                if node.left:
                    next_q1.append(node.left)
                if node.right:
                    next_q1.append(node.right)

            for node in q2:
                level2.append(node.data)
                if node.left:
                    next_q2.append(node.left)
                if node.right:
                    next_q2.append(node.right)

            if sorted(level1) != sorted(level2):
                return False

            q1 = next_q1
            q2 = next_q2

        return not q1 and not q2