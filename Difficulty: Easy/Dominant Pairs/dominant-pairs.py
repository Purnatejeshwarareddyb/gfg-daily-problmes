class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        # code here
        n = len(arr)
        mid = n // 2

        first_half = sorted(arr[:mid])
        second_half = sorted(arr[mid:])

        ans = 0
        j = 0

        for i in range(mid):
            while j < mid and first_half[i] >= 5 * second_half[j]:
                j += 1
            ans += j

        return ans