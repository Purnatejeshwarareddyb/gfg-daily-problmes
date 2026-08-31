class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        # code here
        dp = [0] * (n + 1)
        dp[1] = i

        for j in range(2, n + 1):
            if j % 2 == 0:
                dp[j] = min(dp[j - 1] + i, dp[j // 2] + c)
            else:
                dp[j] = min(dp[j - 1] + i, dp[(j + 1) // 2] + c + d)

        return dp[n]
        