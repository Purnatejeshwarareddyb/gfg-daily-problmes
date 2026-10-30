class Solution:

  def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
    MOD = 10**9 + 7
    freq = {}
    for x in arr:
      freq[x] = freq.get(x, 0) + 1

    # powers of 2 modulo MOD
    def power(base, exp):
      res = 1
      base %= MOD
      while exp > 0:
        if exp % 2 == 1:
          res = (res * base) % MOD
        base = (base * base) % MOD
        exp //= 2
      return res

    ans = 0
    # Condition for MEX = m:
    # 1. For each i in [0, m-1], subset must contain at least one occurrence of i.
    #    Number of ways to choose elements from frequency of i: (2^freq[i] - 1)
    # 2. Subset must NOT contain m.
    # 3. For elements > m, we can either include them or not (2^freq[x] ways for each x > m).

    current_prefix_ways = 1
    for m in range(l, r + 1):
      # Check if all numbers from 0 to m-1 can be included (i.e., they exist in array)
      possible = True
      ways = current_prefix_ways

      for i in range(m):
        if i not in freq:
          possible = False
          break
        ways = (ways * (power(2, freq[i]) - 1)) % MOD

      if not possible:
        # If any number from 0 to m-1 is missing, MEX = m is impossible for any subset,
        # and all subsequent MEX values > m will also be impossible.
        break

      # Multiply by choices for elements strictly greater than m
      excl_ways = 1
      for x in freq:
        if x > m:
          excl_ways = (excl_ways * power(2, freq[x])) % MOD

      total_m = (ways * excl_ways) % MOD
      ans = (ans + total_m) % MOD

    return ans