class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        # code hear
        n = len(arr)
        curr_sum = sum(arr[:k])
        max_sum = curr_sum
        kadane_sum = 0
        
        for i in range(k, n):
            curr_sum += arr[i] - arr[i-k]
            kadane_sum += arr[i-k]
            if kadane_sum < 0:
                kadane_sum = 0
            max_sum = max(max_sum, curr_sum, curr_sum + kadane_sum)
            
        return max_sum
