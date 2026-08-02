class Solution:
    def count(self, n: int, m: int) -> int:
        #code hear
        MOD = 10**9 + 7
        dp = [1] * (m + 1)
        dp[0] = 0
        
        for _ in range(n - 1):
            next_dp = [0] * (m + 1)
            for k in range(1, m + 1):
                next_dp[k] = (next_dp[k] + dp[k]) % MOD
                for j in range(2 * k, m + 1, k):
                    next_dp[j] = (next_dp[j] + dp[k]) % MOD
                    next_dp[k] = (next_dp[k] + dp[j]) % MOD
            dp = next_dp
            
        return sum(dp) % MOD
