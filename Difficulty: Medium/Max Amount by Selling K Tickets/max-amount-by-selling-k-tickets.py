class Solution:
    def maxAmount(self, arr, k):
        # code hear
        # Define the binary search range for the threshold price
        low = 0
        high = max(arr)
        P = high
        
        # Binary search to find the optimal threshold price P
        while low <= high:
            mid = (low + high) // 2
            # Count how many tickets have a price strictly greater than 'mid'
            count = sum(max(0, x - mid) for x in arr)
            
            if count <= k:
                P = mid
                high = mid - 1  # Try to find a smaller valid price threshold
            else:
                low = mid + 1   # Price is too low, resulting in too many tickets
                
        total_revenue = 0
        total_sold = 0
        MOD = 10**9 + 7
        
        # Collect the revenue from all tickets priced strictly above P
        for x in arr:
            if x > P:
                num_tickets = x - P
                total_sold += num_tickets
                # Sum of arithmetic progression from (P + 1) to x
                total_revenue += (x + P + 1) * num_tickets // 2
                
        # Fill any remaining ticket capacity at exactly price P
        remaining_tickets = k - total_sold
        total_revenue += remaining_tickets * P
        
        return total_revenue % MOD
