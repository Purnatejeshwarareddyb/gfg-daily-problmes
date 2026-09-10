class Solution:

    def pairCount(self, x, y):
        """code here"""
        if y % x != 0:
            return 0

        k = y // x
        count = 0

        for i in range(1, int(math.isqrt(k)) + 1):
            if k % i == 0:
                j = k // i
                if math.gcd(i, j) == 1:
                    if i == j:
                        count += 1
                    else:
                        count += 2

        return count