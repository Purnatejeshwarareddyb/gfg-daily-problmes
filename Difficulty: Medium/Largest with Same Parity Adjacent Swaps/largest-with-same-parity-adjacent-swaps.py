class Solution:

    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        n = len(arr)
        ans = list(arr)
        i = 0
        while i < n:
            j = i
            while j < n and (arr[j] + arr[i]) % 2 == 0:
                j += 1
            ans[i:j] = sorted(arr[i:j], reverse=True)
            i = max(i + 1, j)
        return ans