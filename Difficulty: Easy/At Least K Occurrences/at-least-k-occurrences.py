class Solution:

  def firstElementKTime(self, arr: list[int], k: int) -> int:
    counts = {}
    for x in arr:
      counts[x] = counts.get(x, 0) + 1
      if counts[x] == k:
        return x
    return -1