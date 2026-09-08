class Solution:
    def searchWord(self, mat, word):
        # code here
        n = len(mat)
        m = len(mat[0])
        w_len = len(word)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        result = []

        for r in range(n):
            for c in range(m):
                if mat[r][c] == word[0]:
                    found = False
                    for dr, dc in directions:
                        match = True
                        for k in range(1, w_len):
                            nr, nc = r + dr * k, c + dc * k
                            if not (0 <= nr < n and 0 <= nc < m and mat[nr][nc] == word[k]):
                                match = False
                                break
                        if match:
                            found = True
                            break
                    if found:
                        result.append([r, c])

        return result