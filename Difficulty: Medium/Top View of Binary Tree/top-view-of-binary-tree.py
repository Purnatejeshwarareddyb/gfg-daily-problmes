class Solution:
    def topView(self, root):
        # code hear
        
        if not root:
            return []
        hd_map = {}
        queue = [(root, 0)]
        head = 0
        min_hd = 0
        max_hd = 0
        while head < len(queue):
            node, hd = queue[head]
            head += 1
            if hd not in hd_map:
                hd_map[hd] = node.data
                if hd < min_hd:
                    min_hd = hd
                if hd > max_hd:
                    max_hd = hd
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        return [hd_map[i] for i in range(min_hd, max_hd + 1)]
