class Solution:
    def solve(self, n, s):
        # code here
        seen = set()
        occupied = set()
        unattended = set()
        ans = 0

        for char in s:
            if char not in seen:
                seen.add(char)
                if len(occupied) < n:
                    occupied.add(char)
                else:
                    unattended.add(char)
                    ans += 1
            else:
                if char in occupied:
                    occupied.remove(char)

        return ans