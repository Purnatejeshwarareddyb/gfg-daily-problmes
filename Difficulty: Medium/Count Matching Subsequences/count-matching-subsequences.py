class Solution:
    def countWays(self, s1: str, s2: str) -> int:
        # code hear
        n1, n2 = len(s1), len(s2)
        MOD = 10**9 + 7
        
        dp = [0] * (n2 + 1)
        dp[0] = 1
        
        for char in s1:
            for j in range(n2, 0, -1):
                if char == s2[j - 1]:
                    dp[j] = (dp[j] + dp[j - 1]) % MOD
                    
        return dp[n2]
