class Solution:
    def maxSubsetXOR(self, arr):
        # code hear
        n = len(arr)
        index = 0
        for bit in range(31, -1, -1):
            maxInd = index
            maxEle = -1
            for i in range(index, n):
                if (arr[i] & (1 << bit)) != 0 and arr[i] > maxEle:
                    maxEle = arr[i]
                    maxInd = i
            if maxEle == -1:
                continue
            arr[index], arr[maxInd] = arr[maxInd], arr[index]
            maxInd = index
            for i in range(n):
                if i != maxInd and (arr[i] & (1 << bit)) != 0:
                    arr[i] ^= arr[maxInd]
            index += 1
        res = 0
        for i in range(n):
            res ^= arr[i]
        return res
