class Solution:
    def minInsAndDel(self, a, b):
        # code hear
        n, m = len(a), len(b)
        mapping = {val: i for i, val in enumerate(b)}
        
        lis_arr = []
        for val in a:
            if val in mapping:
                idx = mapping[val]
                low, high = 0, len(lis_arr)
                while low < high:
                    mid = (low + high) // 2
                    if lis_arr[mid] < idx:
                        low = mid + 1
                    else:
                        high = mid
                if low < len(lis_arr):
                    lis_arr[low] = idx
                else:
                    lis_arr.append(idx)
                    
        return n + m - 2 * len(lis_arr)
