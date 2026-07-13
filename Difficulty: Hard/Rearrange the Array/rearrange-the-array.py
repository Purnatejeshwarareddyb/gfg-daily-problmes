class Solution:
    def minOperations(self, b):
        # code hear
        
        MOD = 10**9 + 7
        n = len(b)
        visited = [False] * n
        
        # Helper function to compute GCD
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        # Helper function to compute LCM
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        ans = 1
        
        # Find all cycle lengths
        for i in range(n):
            if not visited[i]:
                # Start tracing the cycle
                curr = i
                cycle_length = 0
                while not visited[curr]:
                    visited[curr] = True
                    curr = b[curr] - 1  # 1-based to 0-based indexing
                    cycle_length += 1
                
                # Update the total LCM modulo 10^9 + 7
                ans = lcm(ans, cycle_length) % MOD
                
        return ans

