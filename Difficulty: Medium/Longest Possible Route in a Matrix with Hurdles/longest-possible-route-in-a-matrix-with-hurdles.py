class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        # code hear
        # Edge case If source or destination is blocked
        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1
            
        n = len(mat)
        m = len(mat[0])
        max_len = [-1]
        
        def dfs(r, c, current_len):
            # Target reached by Update max length
            if r == xd and c == yd:
                max_len[0] = max(max_len[0], current_len)
                return
            
            # Mark current cell as visited
            mat[r][c] = 0
            
            # Explore 4 directions of up, down, left, right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                    dfs(nr, nc, current_len + 1)
            
            # Backtrack Unmark current cell
            mat[r][c] = 1

        dfs(xs, ys, 0)
        return max_len[0]
