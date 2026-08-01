class Solution:
    def findMax(self, n, a, b, k):
        # Code hear
        diff = [0] * (n + 1)
        
        for i in range(len(a)):
            diff[a[i]] += k[i]
            if b[i] + 1 < n:
                diff[b[i] + 1] -= k[i]
                
        max_val = 0
        curr_val = 0
        for i in range(n):
            curr_val += diff[i]
            if curr_val > max_val:
                max_val = curr_val
                
        return max_val
