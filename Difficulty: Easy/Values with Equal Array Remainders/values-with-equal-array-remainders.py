class Solution:
    def sameMod(self, arr):
        # code here
        if len(set(arr)) == 1:
            return -1

        g = 0
        first = arr[0]
        for x in arr[1:]:
            a, b = g, abs(x - first)
            while b:
                a, b = b, a % b
            g = a

        count = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                count += 1
                if i * i != g:
                    count += 1
            i += 1

        return count