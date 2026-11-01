class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        dp0 = arr[0]
        dp1 = max(arr[0], arr[0] ** 2)
        ans = dp1

        for i in range(1, n):
            x = arr[i]
            x2 = x ** 2

            new_dp0 = max(x, dp0 + x)
            new_dp2 = max(x2, dp0 + x2)
            new_dp1 = max(x, dp1 + x, new_dp2)

            dp0 = new_dp0
            dp1 = new_dp1
            ans = max(ans, dp1)

        return ans