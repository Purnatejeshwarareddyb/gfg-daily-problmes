class Solution:
    def diffArray(self, arr, opr):
        n = len(arr)
        diff = [0] * (n + 1)
        
        for l, r, v in opr:
            diff[l] += v
            if r + 1 < n:
                diff[r + 1] -= v
                
        current_diff = 0
        for i in range(n):
            current_diff += diff[i]
            arr[i] += current_diff
            
        return arr

