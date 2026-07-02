class Solution:
    def divisibleByK(self, arr, k):
        # code hear
        n = len(arr)
        
        if n >= k:
            return True
            
        dp = [False] * k
        
        for num in arr:
            rem = num % k
            if rem == 0:
                return True
                
            next_dp = dp[:]
            
            next_dp[rem] = True
            
            for i in range(k):
                if dp[i]:
                    next_dp[(i + rem) % k] = True
                    
            dp = next_dp
            
            if dp[0]:
                return True
                
        return dp[0]
