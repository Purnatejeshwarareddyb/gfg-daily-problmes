class Solution:
    def minDeletions(self, arr):
        # code hear
        lis = []
        for x in arr:
            low, high = 0, len(lis)
            while low < high:
                mid = (low + high) // 2
                if lis[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            if low < len(lis):
                lis[low] = x
            else:
                lis.append(x)
        return len(arr) - len(lis)
