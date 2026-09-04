class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        n = len(arr)
        m = min(m, n)

        current_sum = sum(arr[:m])
        max_sum = current_sum

        for i in range(1, n):
            current_sum += arr[(i + m - 1) % n] - arr[i - 1]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum