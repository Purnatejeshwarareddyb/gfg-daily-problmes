''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def numberOfTurns(self, root, p, q):
        # code here
        
        def findLCA(node, p, q):
            if not node:
                return None
            if node.data == p or node.data == q:
                return node
            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)
            if left and right:
                return node
            return left if left else right

        def countTurns(node, target, is_left, turns):
            if not node:
                return -1
            if node.data == target:
                return turns
            
            left_turns = countTurns(node.left, target, True, turns if is_left is True else (turns + 1 if is_left is not None else turns))
            if left_turns != -1:
                return left_turns
                
            right_turns = countTurns(node.right, target, False, turns if is_left is False else (turns + 1 if is_left is not None else turns))
            return right_turns

        lca = findLCA(root, p, q)
        turns = 0
        
        if lca.data == p:
            turns = countTurns(lca.left, q, True, 0)
            if turns == -1:
                turns = countTurns(lca.right, q, False, 0)
        elif lca.data == q:
            turns = countTurns(lca.left, p, True, 0)
            if turns == -1:
                turns = countTurns(lca.right, p, False, 0)
        else:
            p_turns = countTurns(lca.left, p, True, 0)
            if p_turns == -1:
                p_turns = countTurns(lca.right, p, False, 0)
                
            q_turns = countTurns(lca.left, q, True, 0)
            if q_turns == -1:
                q_turns = countTurns(lca.right, q, False, 0)
                
            turns = p_turns + q_turns + 1

        return turns if turns > 0 else -1