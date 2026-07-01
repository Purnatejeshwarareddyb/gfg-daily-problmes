class Solution:
    def maxSumSubarray(self, arr):
        # code hear
        n = len(arr)
        if n == 0:
            return 0
            
        max_no_del = arr[0]
        max_one_del = arr[0]
        max_so_far = arr[0]
        
        for i in range(1, n):
            max_one_del = max(max_one_del + arr[i], max_no_del)
            max_no_del = max(max_no_del + arr[i], arr[i])
            max_so_far = max(max_so_far, max_no_del, max_one_del)
            
        return max_so_far
