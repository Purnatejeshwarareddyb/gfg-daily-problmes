class Solution:
    def getCount(self, n: int) -> int:
        # code hear
        odd_factors_count = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                if i % 2 != 0:
                    odd_factors_count += 1
                if i * i != n and (n // i) % 2 != 0:
                    odd_factors_count += 1
            i += 1
        return odd_factors_count - 1
