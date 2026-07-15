class Solution:
    def bitonic(self, arr):
        # code hear
        n = len(arr)
        if n == 0:
            return 0

        # Arrays to store the length of non-decreasing 
        # subarray from left to right
        inc = [1] * n
        # Arrays to store the length of non-increasing 
        # subarray from right to left
        dec = [1] * n

        # Compute non-decreasing subarray lengths from left
        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                inc[i] = inc[i - 1] + 1

        # Compute non-increasing subarray lengths from right
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                dec[i] = dec[i + 1] + 1

        # Find the maximum length of bitonic subarray
        max_length = 0
        for i in range(n):
            max_length = max(max_length, inc[i] + dec[i] - 1)

        return max_length
