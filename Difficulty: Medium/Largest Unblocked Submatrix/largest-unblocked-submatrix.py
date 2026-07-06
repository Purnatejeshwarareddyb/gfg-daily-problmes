class Solution:
    def largestArea(self, n, m, k, arr):
        # Extract blocked rows and columns, and add boundaries
        rows = [0] + [cell[0] for cell in arr] + [n + 1]
        cols = [0] + [cell[1] for cell in arr] + [m + 1]
        
        # Sort to find consecutive distances
        rows.sort()
        cols.sort()
        
        # Find the maximum consecutive unblocked rows
        max_r_gap = 0
        for i in range(1, len(rows)):
            max_r_gap = max(max_r_gap, rows[i] - rows[i-1] - 1)
            
        # Find the maximum consecutive unblocked columns
        max_c_gap = 0
        for i in range(1, len(cols)):
            max_c_gap = max(max_c_gap, cols[i] - cols[i-1] - 1)
            
        # The largest continuous submatrix area
        return max_r_gap * max_c_gap
