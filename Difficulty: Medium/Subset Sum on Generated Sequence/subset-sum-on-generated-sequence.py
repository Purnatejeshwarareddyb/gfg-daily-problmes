class Solution:
    def isPossible(self, arr, s, x):
        # code here 
        seq = [s]
        curr_sum = s

        for num in arr:
            val = curr_sum + num
            seq.append(val)
            curr_sum += val
            if val > x:
                break

        for i in range(len(seq) - 1, -1, -1):
            if x >= seq[i]:
                x -= seq[i]

        return x == 0