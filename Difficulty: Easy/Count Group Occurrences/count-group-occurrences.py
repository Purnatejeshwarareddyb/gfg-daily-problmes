class Solution:
    def getCount(self, s: str, k: int) -> int:
        from collections import defaultdict

        group_counts = defaultdict(int)
        i = 0
        n = len(s)

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            group_counts[s[i]] += 1
            i = j

        return sum(1 for char, count in group_counts.items() if count == k)