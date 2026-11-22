class Solution:
    def longestSubarrayDivK(self, arr, k):
        rem_index = {0: -1}
        prefix_sum = 0
        max_len = 0

        for i, val in enumerate(arr):
            prefix_sum += val
            rem = ((prefix_sum % k) + k) % k

            if rem in rem_index:
                max_len = max(max_len, i - rem_index[rem])
            else:
                rem_index[rem] = i

        return max_len