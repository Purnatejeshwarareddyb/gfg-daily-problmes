class Solution:
    def findWays(self, grid):
        # code hear
        MOD = 10**9 + 7
        n = len(grid)
        
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        dp[0][0] = [1, grid[0][0]]
        
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                count = 0
                max_adv = 0
                
                if j > 0 and dp[i][j - 1][0] > 0 and grid[i][j - 1] in (1, 3):
                    c_left, m_left = dp[i][j - 1]
                    count = (count + c_left) % MOD
                    max_adv = max(max_adv, m_left)
                
                if i > 0 and dp[i - 1][j][0] > 0 and grid[i - 1][j] in (2, 3):
                    c_top, m_top = dp[i - 1][j]
                    count = (count + c_top) % MOD
                    max_adv = max(max_adv, m_top)
                
                if count > 0:
                    dp[i][j] = [count, max_adv + grid[i][j]]
        
        return dp[n - 1][n - 1]