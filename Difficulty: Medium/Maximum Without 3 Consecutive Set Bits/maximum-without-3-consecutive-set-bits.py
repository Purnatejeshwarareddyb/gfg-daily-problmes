class Solution:

  def maxValue(self, n: int) -> int:
    for i in range(31, 1, -1):
      if (n & (1 << i)) and (n & (1 << (i - 1))) and (n & (1 << (i - 2))):
        n ^= 1 << (i - 2)
    return n