class Solution:
    def countMinOperations(self, arr):
        # code hear
        res = 0
        max_len = 0
        
        for num in arr:
            bits = 0
            while num > 0:
                if num % 2 == 1:
                    res += 1
                bits += 1
                num //= 2
            
            if bits > 0:
                max_len = max(max_len, bits - 1)
                
        return res + max_len