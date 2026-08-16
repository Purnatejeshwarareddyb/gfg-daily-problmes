class Solution:
    def minProd(self, arr):
        # code here
        n = len(arr)
        if n == 1:
            return arr[0]

        neg_count = 0
        zero_count = 0
        min_pos = float("inf")
        max_neg = float("-inf")
        prod = 1

        for x in arr:
            if x == 0:
                zero_count += 1
                continue

            if x < 0:
                neg_count += 1
                max_neg = max(max_neg, x)
            else:
                min_pos = min(min_pos, x)

            prod *= x

        if zero_count == n:
            return 0

        if neg_count % 2 != 0:
            return prod

        if neg_count == 0:
            if zero_count > 0:
                return 0

            return min_pos

        return prod // max_neg
        