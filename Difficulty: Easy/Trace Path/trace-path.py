class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        max_left = max_right = cur_col = 0
        max_up = max_down = cur_row = 0

        for ch in s:
            if ch == 'L':
                cur_col -= 1
            elif ch == 'R':
                cur_col += 1
            elif ch == 'D':
                cur_row -= 1
            elif ch == 'U':
                cur_row += 1

            max_left = min(max_left, cur_col)
            max_right = max(max_right, cur_col)
            max_down = min(max_down, cur_row)
            max_up = max(max_up, cur_row)

        return (max_right - max_left < m) and (max_up - max_down < n)