class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        # code hear
        n = len(h)
        if n == 0:
            return 0
        if n == 1:
            return max(h[0], l[0])
            
        prev2 = max(h[0], l[0])
        prev1 = max(prev2 + l[1], h[1])
        
        for i in range(2, n):
            curr = max(prev1 + l[i], prev2 + h[i])
            prev2 = prev1
            prev1 = curr
            
        return prev1