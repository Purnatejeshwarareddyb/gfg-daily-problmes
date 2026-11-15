class Solution:
    def subsequenceSum(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        total_sum = 0
        power = pow(2, n - 1, MOD)
        for char in s:
            digit = int(char)
            total_sum = (total_sum + digit * power) % MOD
        return total_sum