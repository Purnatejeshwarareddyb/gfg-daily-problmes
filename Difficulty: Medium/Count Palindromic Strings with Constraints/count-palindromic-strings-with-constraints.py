class Solution:
    def palindromicStrings(self, n, k):
        # code here
        MOD = 10**9 + 7
        total_count = 0

        for L in range(1, n + 1):
            m = (L + 1) // 2
            half_distinct = L // 2

            if k >= m:
                # Number of ways to choose distinct characters for the half length (L // 2)
                ways = 1
                for i in range(half_distinct):
                    ways = (ways * (k - i)) % MOD

                # If length is odd, middle character can be any of the remaining (k - half_distinct) characters
                if L % 2 == 1:
                    ways = (ways * (k - half_distinct)) % MOD

                total_count = (total_count + ways) % MOD

        return total_count