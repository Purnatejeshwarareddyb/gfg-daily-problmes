class Solution:
    def findWays(self, matrix, k):
        MOD = 10**9 + 7
        R, C = len(matrix), len(matrix[0])

        # 1. Precompute suffix sums of apples in O(R * C)
        suff = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                suff[r][c] = matrix[r][c] + suff[r+1][c] + suff[r][c+1] - suff[r+1][c+1]

        # 2. Precompute the FIRST valid row and column cut for each cell in O(R * C * (R + C))
        # This replaces the Binary Search from your original approach
        next_r = [[R] * C for _ in range(R)]
        next_c = [[C] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                for nr in range(r + 1, R):
                    if suff[r][c] > suff[nr][c]:
                        next_r[r][c] = nr
                        break
                for nc in range(c + 1, C):
                    if suff[r][c] > suff[r][nc]:
                        next_c[r][c] = nc
                        break

        # 3. Base Case: 1 piece left (0 cuts remaining)
        dp = [[1 if suff[r][c] > 0 else 0 for c in range(C)] for r in range(R)]

        # 4. Bottom-Up DP: Compute for pieces 2 to K in O(K * R * C)
        for _ in range(2, k + 1):
            new_dp = [[0] * C for _ in range(R)]
            row_sum = [[0] * C for _ in range(R + 1)]
            col_sum = [[0] * (C + 1) for _ in range(R)]
            
            # Build rolling suffix sums for O(1) state transitions
            for r in range(R - 1, -1, -1):
                for c in range(C - 1, -1, -1):
                    row_sum[r][c] = (row_sum[r+1][c] + dp[r][c]) % MOD
                    col_sum[r][c] = (col_sum[r][c+1] + dp[r][c]) % MOD

            # Evaluate O(1) transitions using the precomputed boundaries
            for r in range(R):
                for c in range(C):
                    if suff[r][c] > 0:
                        nr, nc = next_r[r][c], next_c[r][c]
                        val = 0
                        if nr < R: val = (val + row_sum[nr][c]) % MOD
                        if nc < C: val = (val + col_sum[r][nc]) % MOD
                        new_dp[r][c] = val
            dp = new_dp

        return dp[0][0]