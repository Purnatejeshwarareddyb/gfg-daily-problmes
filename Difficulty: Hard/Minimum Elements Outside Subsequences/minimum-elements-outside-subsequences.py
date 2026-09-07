class Solution:
    def minCount(self, arr):
        """ code here """
        n = len(arr)
        memo = {}

        def solve(idx, last_inc, last_dec):
            if idx == n:
                return 0

            state = (idx, last_inc, last_dec)
            if state in memo:
                return memo[state]

            val = arr[idx]

            res = 1 + solve(idx + 1, last_inc, last_dec)

            if val > last_inc:
                res = min(res, solve(idx + 1, val, last_dec))

            if val < last_dec:
                res = min(res, solve(idx + 1, last_inc, val))

            memo[state] = res
            return res

        return solve(0, 0, 101)
