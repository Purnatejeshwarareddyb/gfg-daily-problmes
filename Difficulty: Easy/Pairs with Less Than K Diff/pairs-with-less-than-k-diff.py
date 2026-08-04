class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        # code hear
        
        arr.sort()
        n = len(arr)
        count = 0
        j = 0
        
        for i in range(n):
            while j < n and arr[j] - arr[i] < k:
                j += 1
            count += (j - i - 1)
            
        return count
