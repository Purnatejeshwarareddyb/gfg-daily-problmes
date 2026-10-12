class Solution:
    def minSquares(self, n, m):
        # code here
        def count(n, m):
            n, m = min(n, m), max(n, m)
            if n == m:
                return 1
            elif n == 1:
                return m
            return count(m-n, n) + 1

        return count(n, m)
