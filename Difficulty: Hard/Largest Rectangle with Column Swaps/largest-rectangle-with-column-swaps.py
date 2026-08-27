class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])

        hist = [[0] * m for _ in range(n)]

        for j in range(m):
            hist[0][j] = mat[0][j]
            for i in range(1, n):
                if mat[i][j] == 1:
                    hist[i][j] = hist[i - 1][j] + 1
                else:
                    hist[i][j] = 0

        max_area = 0

        for i in range(n):
            count = [0] * (n + 1)
            for j in range(m):
                count[hist[i][j]] += 1

            col_count = 0
            for h in range(n, 0, -1):
                col_count += count[h]
                area = h * col_count
                if area > max_area:
                    max_area = area

        return max_area