class Solution:
    def countWays(self, n, m):
        # code hear
        if n < m:
            return 1
        
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        
        for i in range(1, m):
            dp[i] = 1
        dp[m] = 2
        
        for i in range(m + 1, n + 1):
            dp[i] = (dp[i-1] + dp[i-m]) % MOD
            
        return dp[n]
