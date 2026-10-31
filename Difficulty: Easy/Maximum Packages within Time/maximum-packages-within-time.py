class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        n = len(arr)
        if totalTime >= n:
            return sum(arr)

        current_sum = sum(arr[:totalTime])
        max_sum = current_sum

        for i in range(totalTime, n):
            current_sum += arr[i] - arr[i - totalTime]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum