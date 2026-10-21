class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        min_so_far = current_min = arr[0]
        for x in arr[1:]:
            current_min = min(x, current_min + x)
            min_so_far = min(min_so_far, current_min)
        return min_so_far