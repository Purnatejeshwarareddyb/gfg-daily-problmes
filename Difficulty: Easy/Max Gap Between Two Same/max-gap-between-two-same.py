class Solution:
    def maxCharGap(self, s: str) -> int:
        # code hear
        first_occurrence = {}
        max_gap = -1
        
        for i, char in enumerate(s):
            if char in first_occurrence:
                # Calculate the characters between the two occurrences
                gap = i - first_occurrence[char] - 1
                if gap > max_gap:
                    max_gap = gap
            else:
                # Record the first time we see this character
                first_occurrence[char] = i
                
        return max_gap
