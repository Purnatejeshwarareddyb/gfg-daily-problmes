class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (1 if s[i] in vowels else 0)
        res = []
        for l, r in queries:
            res.append(pref[r + 1] - pref[l])
        return res