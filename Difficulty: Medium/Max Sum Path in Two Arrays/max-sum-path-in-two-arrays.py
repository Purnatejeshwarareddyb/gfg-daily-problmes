class Solution:
    def maxPathSum(self, a, b):
        i, j = 0, 0
        n, m = len(a), len(b)
        
        # Track sums of elements between common intersection points
        sum1, sum2 = 0, 0
        total_sum = 0
        
        while i < n and j < m:
            if a[i] < b[j]:
                sum1 += a[i]
                i += 1
            elif a[i] > b[j]:
                sum2 += b[j]
                j += 1
            else:
                # Common element found: take the max path before this point
                total_sum += max(sum1, sum2) + a[i]
                # Reset segment sums
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1
                
        # Collect remaining elements from array a, if any
        while i < n:
            sum1 += a[i]
            i += 1
            
        # Collect remaining elements from array b, if any
        while j < m:
            sum2 += b[j]
            j += 1
            
        # Add the maximum of the remaining paths
        total_sum += max(sum1, sum2)
        
        return total_sum
