class Solution:
    def maxIndexDifference(self, s):
        # code hear
        n = len(s)
        
        seen_right = set()
        next_exists = [False] * n
        for i in range(n - 1, -1, -1):
            next_char = chr(ord(s[i]) + 1)
            if next_char in seen_right:
                next_exists[i] = True
            seen_right.add(s[i])
            
        best_start = [float('inf')] * 26
        max_diff = -1
        
        for i, char in enumerate(s):
            val = ord(char) - ord('a')
            
            if val == 0:
                start = i
            else:
                start = best_start[val - 1]
                
            if start != float('inf'):
                if not next_exists[i]:
                    max_diff = max(max_diff, i - start)
                
                best_start[val] = min(best_start[val], start)
                
        return max_diff
