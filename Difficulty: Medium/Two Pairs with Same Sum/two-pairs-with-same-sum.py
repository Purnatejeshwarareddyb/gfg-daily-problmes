class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        sum_map = {}
        ans = None

        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                if s in sum_map:
                    a, b = sum_map[s]
                    if a != i and a != j and b != i and b != j:
                        cand = [a, b, i, j]
                        if ans is None or cand < ans:
                            ans = cand
                else:
                    sum_map[s] = (i, j)

        return ans if ans is not None else [-1, -1, -1, -1]