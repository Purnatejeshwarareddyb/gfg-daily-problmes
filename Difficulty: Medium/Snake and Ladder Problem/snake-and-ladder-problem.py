class Solution:
    def minThrows(self, n, lad, sn):
        # code here
        target = n * n
        board = {}

        for i in range(0, len(lad), 2):
            board[lad[i]] = lad[i + 1]

        for i in range(0, len(sn), 2):
            board[sn[i]] = sn[i + 1]

        queue = [(1, 0)]
        visited = {1}

        for curr, throws in queue:
            if curr == target:
                return throws

            for dice in range(1, 7):
                nxt = curr + dice
                if nxt <= target:
                    if nxt in board:
                        nxt = board[nxt]

                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, throws + 1))

        return -1
        