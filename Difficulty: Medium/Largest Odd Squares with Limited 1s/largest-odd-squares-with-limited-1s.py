class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        # code hear
        n = len(mat)
        m = len(mat[0])
        
        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for r in range(n):
            for c in range(m):
                pref[r + 1][c + 1] = mat[r][c] + pref[r][c + 1] + pref[r + 1][c] - pref[r][c]
                
        def get_sum(r1, c1, r2, c2):
            return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]

        res = []
        for r, c in queries:
            if mat[r][c] > k:
                res.append(-1)
                continue
                
            max_d = min(r, n - 1 - r, c, m - 1 - c)
            
            low, high = 0, max_d
            ans = 0
            
            while low <= high:
                mid = (low + high) // 2
                count_ones = get_sum(r - mid, c - mid, r + mid, c + mid)
                if count_ones <= k:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
                    
            res.append(2 * ans + 1)
            
        return res