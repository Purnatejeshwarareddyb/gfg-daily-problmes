class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        # code hear
        
        def countAtMost(max_sum: int) -> int:
            if max_sum < 0:
                return 0
            res = 0
            left = 0
            current_sum = 0
            for right in range(len(arr)):
                current_sum += arr[right]
                while current_sum > max_sum:
                    current_sum -= arr[left]
                    left += 1
                res += (right - left + 1)
            return res
        
        return countAtMost(r) - countAtMost(l - 1)
