class Solution:
    def countKdivPairs(self, arr, k):
        # code hear
        rem_counts = {}
        pair_count = 0
        
        for num in arr:
            rem = num % k
            complement = (k - rem) % k
            
            if complement in rem_counts:
                pair_count += rem_counts[complement]
                
            rem_counts[rem] = rem_counts.get(rem, 0) + 1
            
        return pair_count
