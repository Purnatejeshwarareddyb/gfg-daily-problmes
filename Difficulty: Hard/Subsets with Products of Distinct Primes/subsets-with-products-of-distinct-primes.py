class Solution:
    def countSubsets(self, arr):
        # code hear
        
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_to_index = {p: i for i, p in enumerate(primes)}
        
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
            
        num_mask = {}
        for i in range(2, 31):
            temp = i
            mask = 0
            possible = True
            for p in primes:
                if temp % p == 0:
                    count = 0
                    while temp % p == 0:
                        count += 1
                        temp //= p
                    if count > 1:
                        possible = False
                        break
                    mask |= (1 << prime_to_index[p])
            if possible:
                num_mask[i] = mask

        dp = {0: 1}
        for num in range(2, 31):
            if num not in num_mask or num not in freq:
                continue
            mask = num_mask[num]
            count = freq[num]
            
            next_dp = dp.copy()
            for prev_mask, prev_count in dp.items():
                if (prev_mask & mask) == 0:
                    new_mask = prev_mask | mask
                    next_dp[new_mask] = (next_dp.get(new_mask, 0) + prev_count * count) % MOD
            dp = next_dp

        total = sum(v for k, v in dp.items() if k > 0) % MOD
        
        if 1 in freq:
            total = (total * pow(2, freq[1], MOD)) % MOD
            
        return total
