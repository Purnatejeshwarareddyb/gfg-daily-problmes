class Solution:

  def goodIndices(self, arr):
    n = len(arr)
    memo = [0] * n 

    def dfs(i):
      if i < 0 or i >= n:
        return True
      if memo[i] == 2:
        return True
      if memo[i] == -1 or memo[i] == 1:
        return False

      memo[i] = 1
      next_idx = i + arr[i]
      is_good = dfs(next_idx)

      memo[i] = 2 if is_good else -1
      return is_good

    for i in range(n):
      if memo[i] == 0:
        dfs(i)

    return sum(1 for i in range(n) if memo[i] == 2)