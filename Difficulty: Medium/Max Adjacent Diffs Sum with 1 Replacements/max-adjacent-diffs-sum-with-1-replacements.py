class Solution:
    def maxDiffSum(self, arr):
        # code here
        n = len(arr)
        if n <= 1:
            return 0

        dp0 = 0  # Max sum ending with arr[0] unchanged
        dp1 = 0  # Max sum ending with arr[0] replaced by 1

        for i in range(1, n):
            new_dp0 = max(dp0 + abs(arr[i] - arr[i - 1]), dp1 + abs(arr[i] - 1))
            new_dp1 = max(dp0 + abs(1 - arr[i - 1]), dp1 + abs(1 - 1))

            dp0, dp1 = new_dp0, new_dp1

        return max(dp0, dp1)