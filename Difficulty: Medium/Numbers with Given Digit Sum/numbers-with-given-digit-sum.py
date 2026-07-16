class Solution:
    def countWays(self, n, sum):
        # code hear
        
        if sum < 1 or sum > 9 * n:
            return -1
        if n == 1:
            return 1 if sum <= 9 else -1
        dp = [[0] * (sum + 1) for _ in range(n)]
        for j in range(10):
            if j <= sum:
                dp[0][j] = 1
        for i in range(1, n - 1):
            for j in range(sum + 1):
                for d in range(10):
                    if j >= d:
                        dp[i][j] += dp[i - 1][j - d]
        ans = 0
        for d in range(1, 10):
            if sum >= d:
                ans += dp[n - 2][sum - d]
        return ans if ans > 0 else -1
