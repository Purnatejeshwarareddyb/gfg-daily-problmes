class Solution:
    def levelSort(self, arr):
        # code hear
        
        res = []
        n = len(arr)
        start = 0
        level_size = 1
        
        while start < n:
            end = min(start + level_size, n)
            level = arr[start:end]
            
            level.sort()
            res.append(level)
            
            start = end
            level_size *= 2
            
        return res
