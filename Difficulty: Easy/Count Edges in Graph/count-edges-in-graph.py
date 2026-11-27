class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        # code here
        total = 0
        for neighbors in adj:
            total += len(neighbors)
        return total // 2