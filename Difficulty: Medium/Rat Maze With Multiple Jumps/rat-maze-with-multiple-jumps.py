class Solution:
    def shortestDist(self, mat):
        n = len(mat)
        ans = [[0] * n for _ in range(n)]
        # memo[r][c] stores True/False if a path is possible from (r, c)
        memo = [[None] * n for _ in range(n)]
        
        def solve(r, c):
            # Base case: destination reached
            if r == n - 1 and c == n - 1:
                ans[r][c] = 1
                return True
                
            # Check memoized result to avoid redundant work
            if memo[r][c] is not None:
                return memo[r][c]
                
            # If cell is blocked
            if mat[r][c] == 0:
                memo[r][c] = False
                return False
                
            max_jump = mat[r][c]
            
            # Try shorter jump lengths first
            for jump in range(1, max_jump + 1):
                # Move Forward (Right)
                if c + jump < n:
                    ans[r][c] = 1
                    if solve(r, c + jump):
                        memo[r][c] = True
                        return True
                    ans[r][c] = 0  # Backtrack
                    
                # Move Downward
                if r + jump < n:
                    ans[r][c] = 1
                    if solve(r + jump, c):
                        memo[r][c] = True
                        return True
                    ans[r][c] = 0  # Backtrack
            
            # Mark as failing if no jumps from this cell found a path
            memo[r][c] = False
            return False

        if solve(0, 0):
            return ans
        return [[-1]]
