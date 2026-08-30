class Solution:

    def getMarks(self, l, r, rank):
        """code here"""
        n = len(l)
        pref = [0] * n
        curr_sum = 0

        for i in range(n):
            curr_sum += (r[i] - l[i] + 1)
            pref[i] = curr_sum

        ans = []
        for k in rank:
            # Manual binary search (bisect_left)
            low, high = 0, n - 1
            idx = n
            while low <= high:
                mid = (low + high) // 2
                if pref[mid] >= k:
                    idx = mid
                    high = mid - 1
                else:
                    low = mid + 1

            prev_count = pref[idx - 1] if idx > 0 else 0
            offset = k - prev_count - 1
            ans.append(l[idx] + offset)

        return ans
        