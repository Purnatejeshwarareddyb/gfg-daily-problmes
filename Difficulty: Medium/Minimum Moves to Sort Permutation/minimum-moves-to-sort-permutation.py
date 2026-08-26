class Solution:
    def minMoves(self, arr):
        """code here"""
        n = len(arr)
        dp = {}
        max_len = 0
        for x in arr:
            dp[x] = dp.get(x - 1, 0) + 1
            if dp[x] > max_len:
                max_len = dp[x]
        return n - max_len