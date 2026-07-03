class Solution:
    def countSubstring(self, s: str) -> int:
        # code hear
        n = len(s)
        # Shift offset to handle negative prefix sums safely
        offset = n + 1
        # Size of BIT array to cover the range from -n to n
        bit = [0] * (2 * n + 5)
        
        def update(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            total = 0
            while idx > 0:
                total += bit[idx]
                idx -= idx & (-idx)
            return total

        ans = 0
        curr_sum = 0
        
        # Add the initial prefix sum (0) before processing characters
        update(0 + offset, 1)
        
        for char in s:
            # Convert '1' to +1 and '0' to -1
            if char == '1':
                curr_sum += 1
            else:
                curr_sum -= 1
            
            # Count all previous prefix sums strictly less than the current prefix sum
            ans += query(curr_sum + offset - 1)
            
            # Store the current prefix sum in the BIT
            update(curr_sum + offset, 1)
            
        return ans
