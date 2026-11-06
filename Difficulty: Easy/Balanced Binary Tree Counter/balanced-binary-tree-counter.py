class Solution:

  def countBT(self, h: int) -> int:
    MOD = 10**9 + 7
    if h == 0 or h == 1:
      return 1
    dp = [0] * (h + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, h + 1):
      dp[i] = (dp[i - 1] * (2 * dp[i - 2] + dp[i - 1])) % MOD
    return dp[h]