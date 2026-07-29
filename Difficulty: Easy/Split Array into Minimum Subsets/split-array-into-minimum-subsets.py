class Solution:
    def minSubsets(self, arr):
        #code here
        arr.sort()
        
        if not arr:
            return 0
            
        count = 1
        
        
        for i in range(len(arr)-1):
            if arr[i] + 1 != arr[i+1]:
                count += 1
        
        return count