class Solution:
    def minFlips(self, s):
        flips_start_0 = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                flips_start_0 += 1
        return min(flips_start_0, len(s) - flips_start_0)