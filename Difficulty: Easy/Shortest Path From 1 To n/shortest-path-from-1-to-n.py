class Solution:
    def minimumStep(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1
            ans += 1
        return ans