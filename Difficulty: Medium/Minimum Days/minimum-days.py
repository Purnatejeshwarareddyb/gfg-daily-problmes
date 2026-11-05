class Solution:

  def getMinimumDays(self, s: str, p: list[int]) -> int:
    s_list = list(s)
    n = len(s)
    match_count = 0

    for i in range(n - 1):
      if s_list[i] != "?" and s_list[i] == s_list[i + 1]:
        match_count += 1

    if match_count == 0:
      return 0

    for day, idx in enumerate(p):
      if s_list[idx] != "?":
        if idx - 1 >= 0 and s_list[idx - 1] == s_list[idx]:
          match_count -= 1
        if idx + 1 < n and s_list[idx + 1] == s_list[idx]:
          match_count -= 1
        s_list[idx] = "?"

      if match_count == 0:
        return day + 1

    return 0