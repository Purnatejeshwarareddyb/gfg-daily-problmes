class Solution:

  def countAlwaysFound(self, arr):
    n = len(arr)
    left_max = [0] * n
    right_min = [0] * n

    cur_max = -1
    for i in range(n):
      cur_max = max(cur_max, arr[i])
      left_max[i] = cur_max

    cur_min = float('inf')
    for i in range(n - 1, -1, -1):
      cur_min = min(cur_min, arr[i])
      right_min[i] = cur_min

    count = 0
    for i in range(n):
      is_larger_than_left = i == 0 or arr[i] > left_max[i - 1]
      is_smaller_than_right = i == n - 1 or arr[i] < right_min[i + 1]
      if is_larger_than_left and is_smaller_than_right:
        count += 1
    return count