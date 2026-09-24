class Solution:
    def maxStackHeight(self, r, h):
        # code here

        MAX_VAL = 1000
        tree = [0] * (MAX_VAL + 1)

        def update(idx, val):
            while idx <= MAX_VAL:
                if val > tree[idx]:
                    tree[idx] = val
                idx += idx & (-idx)

        def query(idx):
            max_val = 0
            while idx > 0:
                if tree[idx] > max_val:
                    max_val = tree[idx]
                idx -= idx & (-idx)
            return max_val

        discs = sorted(zip(r, h), key=lambda x: x[0])
        n = len(discs)
        max_total_height = 0

        i = 0
        while i < n:
            j = i
            while j < n and discs[j][0] == discs[i][0]:
                j += 1

            dp_values = []
            for k in range(i, j):
                radius, height = discs[k]
                best_prev = query(height - 1)
                dp_values.append(best_prev + height)

            for k in range(i, j):
                height = discs[k][1]
                val = dp_values[k - i]
                update(height, val)
                if val > max_total_height:
                    max_total_height = val

            i = j

        return max_total_height