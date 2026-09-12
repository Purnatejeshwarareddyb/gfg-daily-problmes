class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        # code here
        arr.sort()
        n = len(arr)

        if arr[n - 1] <= 0 and k % 2 != 0:
            prod = 1
            for i in range(n - 1, n - 1 - k, -1):
                prod *= arr[i]
            return prod

        prod = 1
        i = 0
        j = n - 1

        if k % 2 != 0:
            prod *= arr[j]
            j -= 1
            k -= 1

        while k > 0:
            left_prod = arr[i] * arr[i + 1]
            right_prod = arr[j] * arr[j - 1]

            if left_prod > right_prod:
                prod *= left_prod
                i += 2
            else:
                prod *= right_prod
                j -= 2
            k -= 2

        return prod