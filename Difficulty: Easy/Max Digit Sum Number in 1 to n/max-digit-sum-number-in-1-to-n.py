class Solution:
    def findMax(self, n):
        # code here
        s = str(n)
        ans = n
        max_sum = sum(int(d) for d in s)

        current = list(s)
        for i in range(len(s)):
            if current[i] == '0':
                continue
            temp = list(current)
            temp[i] = str(int(temp[i]) - 1)
            for j in range(i + 1, len(s)):
                temp[j] = '9'

            val = int(''.join(temp))
            digit_sum = sum(int(d) for d in str(val))

            if digit_sum > max_sum or (digit_sum == max_sum and val > ans):
                max_sum = digit_sum
                ans = val

        return ans