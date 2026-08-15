class Solution:

    def countWithout(self, n: int, d: int) -> int:
        # code here
        s = str(n)
        m = len(s)

        memo = {}

        def solve(idx, is_less, is_started):
            if idx == m:
                return 1 if is_started else 0

            state = (idx, is_less, is_started)
            if state in memo:
                return memo[state]

            limit = 9 if is_less else int(s[idx])
            ans = 0

            for digit in range(limit + 1):
                if is_started or digit != 0:
                    if digit == d:
                        continue
                    ans += solve(idx + 1, is_less or (digit < limit), True)
                else:
                    ans += solve(idx + 1, True, False)

            memo[state] = ans
            return ans

        return solve(0, False, False)