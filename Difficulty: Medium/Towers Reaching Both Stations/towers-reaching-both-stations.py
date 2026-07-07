class Solution:
    def countCoordinates(self, mat: list[list[int]]) -> int:
        # code hear
        if not mat or not mat[0]:
            return 0
            
        n = len(mat)
        m = len(mat[0])
        
        # Keep track of towers that can reach each station
        p_visited = [[False] * m for _ in range(n)]
        q_visited = [[False] * m for _ in range(n)]
        
        def dfs(r: int, c: int, visited: list[list[bool]]):
            visited[r][c] = True
            # Check all four cardinal directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # Check boundaries and if already visited
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    # Signal can move to nr, nc if its strength is >= current cell
                    if mat[nr][nc] >= mat[r][c]:
                        dfs(nr, nc, visited)
                        
        # Traverse from Station P boundaries (Top and Left)
        for j in range(m):
            if not p_visited[0][j]:
                dfs(0, j, p_visited)
        for i in range(n):
            if not p_visited[i][0]:
                dfs(i, 0, p_visited)
                
        # Traverse from Station Q boundaries (Bottom and Right)
        for j in range(m):
            if not q_visited[n - 1][j]:
                dfs(n - 1, j, q_visited)
        for i in range(n):
            if not q_visited[i][m - 1]:
                dfs(i, m - 1, q_visited)
                
        # Count towers reaching both stations
        count = 0
        for i in range(n):
            for j in range(m):
                if p_visited[i][j] and q_visited[i][j]:
                    count += 1
                    
        return count
