class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        low, high = 1, min(s1, s2) * n
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if (mid // s1) + (mid // s2) >= n:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans