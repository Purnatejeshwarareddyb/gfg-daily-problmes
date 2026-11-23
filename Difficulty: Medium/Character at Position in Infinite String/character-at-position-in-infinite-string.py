class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        n = len(s)
        if pos <= n:
            return s[pos - 1]

        lengths = [n]
        step = 1
        while lengths[-1] < pos:
            lengths.append(2 * lengths[-1] + step)
            step += 1

        for idx in range(len(lengths) - 1, 0, -1):
            prev_len = lengths[idx - 1]
            dollar_count = idx
            if pos <= prev_len:
                continue
            elif pos <= prev_len + dollar_count:
                return '$'
            else:
                rev_idx = pos - (prev_len + dollar_count) - 1
                pos = prev_len - rev_idx

        return s[pos - 1]