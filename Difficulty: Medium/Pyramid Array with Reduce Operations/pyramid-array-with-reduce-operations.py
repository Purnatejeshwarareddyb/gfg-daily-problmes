class Solution:
    def formPyramid(self, arr):
        # code here 

        n = len(arr)

        left = [0] * n
        right = [0] * n

        left[0] = 1
        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1] + 1)

        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1] + 1)

        total_sum = sum(arr)
        max_pyramid_sum = 0

        for i in range(n):
            h = min(left[i], right[i])
            pyramid_sum = h * h
            max_pyramid_sum = max(max_pyramid_sum, pyramid_sum)

        return total_sum - max_pyramid_sum