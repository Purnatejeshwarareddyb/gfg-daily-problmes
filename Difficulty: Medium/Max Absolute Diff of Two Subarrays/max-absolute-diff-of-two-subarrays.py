class Solution:
    def maxDiffSubArrays(self, arr):
        n = len(arr)
        if n < 2:
            return 0
            
        # Initialize arrays to store max/min subarray sums from left and right
        left_max = [0] * n
        left_min = [0] * n
        right_max = [0] * n
        right_min = [0] * n
        
        # 1. Forward Pass (Left to Right)
        current_max = arr[0]
        max_so_far = arr[0]
        current_min = arr[0]
        min_so_far = arr[0]
        
        left_max[0] = max_so_far
        left_min[0] = min_so_far
        
        for i in range(1, n):
            current_max = max(arr[i], current_max + arr[i])
            max_so_far = max(max_so_far, current_max)
            left_max[i] = max_so_far
            
            current_min = min(arr[i], current_min + arr[i])
            min_so_far = min(min_so_far, current_min)
            left_min[i] = min_so_far
            
        # 2. Backward Pass (Right to Left)
        current_max = arr[n - 1]
        max_so_far = arr[n - 1]
        current_min = arr[n - 1]
        min_so_far = arr[n - 1]
        
        right_max[n - 1] = max_so_far
        right_min[n - 1] = min_so_far
        
        for i in range(n - 2, -1, -1):
            current_max = max(arr[i], current_max + arr[i])
            max_so_far = max(max_so_far, current_max)
            right_max[i] = max_so_far
            
            current_min = min(arr[i], current_min + arr[i])
            min_so_far = min(min_so_far, current_min)
            right_min[i] = min_so_far
            
        # 3. Find Maximum Absolute Difference
        max_diff = float('-inf')
        for i in range(n - 1):
            # Case 1: Max from left, Min from right
            diff1 = abs(left_max[i] - right_min[i + 1])
            # Case 2: Min from left, Max from right
            diff2 = abs(left_min[i] - right_max[i + 1])
            
            max_diff = max(max_diff, diff1, diff2)
            
        return max_diff
