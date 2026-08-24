class Solution:
    def prefixStrings(self, n: int) -> int:
        # code here
        MOD = 10**9 + 7

        # Calculate N-th Catalan Number: C_n = (1 / (n + 1)) * (2n choose n) % MOD
        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        def modInverse(n):
            return power(n, MOD - 2)

        fact = [1] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        numerator = fact[2 * n]
        denominator = (fact[n + 1] * fact[n]) % MOD

        return (numerator * modInverse(denominator)) % MOD