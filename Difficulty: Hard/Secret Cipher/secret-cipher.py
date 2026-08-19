class Solution:
    def compress(self, s):
        # code here
        n = len(s)
        # Compute KMP prefix function (LPS array) for the string s
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
            lps[i] = j

        res = []
        i = n - 1

        # Process the string from right to left to greedily apply '*' compression
        while i >= 0:
            if (i + 1) % 2 == 0:
                half = (i + 1) // 2
                cur = lps[i]

                # Check if the prefix of length half matches the suffix of length half ending at i
                while cur > half:
                    cur = lps[cur - 1]

                if cur == half:
                    res.append('*')
                    i = half - 1
                    continue

            res.append(s[i])
            i -= 1

        return "".join(reversed(res))