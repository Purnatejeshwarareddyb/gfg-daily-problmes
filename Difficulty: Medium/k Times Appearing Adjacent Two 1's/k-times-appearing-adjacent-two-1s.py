class Solution:
    def countStrings(self, n, k):
        if k >= n:
            return 0
        MOD = 10**9 + 7
        dp = [[0, 0] for _ in range(k + 1)]
        dp[0][0] = 1
        dp[0][1] = 1
        
        for i in range(2, n + 1):
            next_dp = [[0, 0] for _ in range(k + 1)]
            for j in range(k + 1):
                next_dp[j][0] = (dp[j][0] + dp[j][1]) % MOD
                next_dp[j][1] = dp[j][0]
                if j > 0:
                    next_dp[j][1] = (next_dp[j][1] + dp[j-1][1]) % MOD
            dp = next_dp
            
        return (dp[k][0] + dp[k][1]) % MOD
