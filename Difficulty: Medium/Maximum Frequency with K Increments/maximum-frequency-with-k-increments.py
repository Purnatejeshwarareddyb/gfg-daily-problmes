class Solution:
    def maxFrequency(self, arr: list[int], k: int) -> int:
        arr.sort()
        left = 0
        total = 0
        ans = 1

        for right in range(len(arr)):
            total += arr[right]

            while (right - left + 1) * arr[right] - total > k:
                total -= arr[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans