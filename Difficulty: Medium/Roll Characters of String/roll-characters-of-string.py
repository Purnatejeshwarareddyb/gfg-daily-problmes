class Solution:
    def findRollOut(self, s, roll):
        n = len(s)
        freq = [0] * (n + 1)
        for r in roll:
            freq[0] += 1
            freq[r] -= 1

        res = []
        curr_rolls = 0
        for i in range(n):
            curr_rolls += freq[i]
            total_shift = (ord(s[i]) - ord('a') + curr_rolls) % 26
            res.append(chr(ord('a') + total_shift))

        return "".join(res)