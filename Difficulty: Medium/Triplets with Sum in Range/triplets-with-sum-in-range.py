class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        arr.sort()

        def countLessEqual(val):
            count = 0
            n = len(arr)
            for i in range(n - 2):
                left = i + 1
                right = n - 1
                while left < right:
                    if arr[i] + arr[left] + arr[right] <= val:
                        count += (right - left)
                        left += 1
                    else:
                        right -= 1
            return count

        return countLessEqual(r) - countLessEqual(l - 1)