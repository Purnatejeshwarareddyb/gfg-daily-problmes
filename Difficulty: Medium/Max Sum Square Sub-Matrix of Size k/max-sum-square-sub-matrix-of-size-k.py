class Solution:
    def maximumSum(self, mat, k):
        # code hear
        n = len(mat)
        p = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                p[i][j] = mat[i-1][j-1] + p[i-1][j] + p[i][j-1] - p[i-1][j-1]
                
        max_sum = float('-inf')
        
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                curr_sum = p[i+k][j+k] - p[i][j+k] - p[i+k][j] + p[i][j]
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    
        return max_sum
