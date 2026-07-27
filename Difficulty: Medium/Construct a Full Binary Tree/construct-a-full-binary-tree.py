''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructBinaryTree(self, pre, preMirror):
        def construct(pre_start, pre_end, mirror_start, mirror_end):
            if pre_start > pre_end:
                return None
            
            root = Node(pre[pre_start])
            if pre_start == pre_end:
                return root
            
            left_val = pre[pre_start + 1]
            left_root_idx = mirror_map[left_val]
            
            num_elements = mirror_end - left_root_idx + 1
            
            root.left = construct(pre_start + 1, pre_start + num_elements, left_root_idx, mirror_end)
            root.right = construct(pre_start + num_elements + 1, pre_end, mirror_start + 1, left_root_idx - 1)
            
            return root

        mirror_map = {val: i for i, val in enumerate(preMirror)}
        return construct(0, len(pre) - 1, 0, len(preMirror) - 1)
