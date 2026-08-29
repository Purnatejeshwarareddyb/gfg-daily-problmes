class Solution:
    def countSubsequences(self, s, n):
        # code here
        MOD = 10**9 + 7
        dp = [0] * n

        for char in s:
            digit = int(char)
            next_dp = dp[:]

            # Include char as the start of a new subsequence
            next_dp[digit % n] = (next_dp[digit % n] + 1) % MOD

            # Append char to existing subsequences
            for rem in range(n):
                if dp[rem] > 0:
                    new_rem = (rem * 10 + digit) % n
                    next_dp[new_rem] = (next_dp[new_rem] + dp[rem]) % MOD

            dp = next_dp

        return dp[0]