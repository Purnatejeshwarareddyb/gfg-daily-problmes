class Solution:

    def minCost(self, mat):
        """code here"""
        n = len(mat)
        if n == 0:
            return 0

        dp0, dp1, dp2 = mat[0][0], mat[0][1], mat[0][2]

        for i in range(1, n):
            new_dp0 = mat[i][0] + min(dp1, dp2)
            new_dp1 = mat[i][1] + min(dp0, dp2)
            new_dp2 = mat[i][2] + min(dp0, dp1)

            dp0, dp1, dp2 = new_dp0, new_dp1, new_dp2

        return min(dp0, dp1, dp2)