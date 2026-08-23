from collections import deque

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[str]]) -> int:
        n = len(mat)
        m = len(mat[0]) if n > 0 else 0

        if n == 0 or m == 0 or mat[r][c] == '#':
            return 0

        # Track minimum (up_moves, down_moves) used to reach each cell
        dist = [[(float('inf'), float('inf')) for _ in range(m)] for _ in range(n)]

        queue = deque([(r, c, 0, 0)])
        dist[r][c] = (0, 0)

        visited_count = 0
        visited = [[False] * m for _ in range(n)]

        # Directions: Up, Down, Left, Right
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while queue:
            curr_r, curr_c, curr_u, curr_d = queue.popleft()

            if not visited[curr_r][curr_c]:
                visited[curr_r][curr_c] = True
                visited_count += 1

            for i in range(4):
                nr, nc = curr_r + dr[i], curr_c + dc[i]

                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == '.':
                    next_u = curr_u + (1 if dr[i] == -1 else 0)
                    next_d = curr_d + (1 if dr[i] == 1 else 0)

                    if next_u <= u and next_d <= d:
                        # Relaxation step based on total vertical moves
                        if next_u + next_d < dist[nr][nc][0] + dist[nr][nc][1]:
                            dist[nr][nc] = (next_u, next_d)
                            queue.append((nr, nc, next_u, next_d))

        return visited_count