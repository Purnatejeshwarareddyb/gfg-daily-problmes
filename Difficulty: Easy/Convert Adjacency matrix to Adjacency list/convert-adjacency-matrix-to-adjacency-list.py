class Solution:
    def matToAdj(self, mat):
        # code here
        return [[j for j, val in enumerate(row) if val == 1] for row in mat]
