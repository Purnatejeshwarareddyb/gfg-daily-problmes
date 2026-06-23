class Solution:
    def maxPeopleDefeated(self, p):
        #code hear
        low, high = 1, 100000
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            s = mid * (mid + 1) * (2 * mid + 1) // 6
            if s <= p:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans