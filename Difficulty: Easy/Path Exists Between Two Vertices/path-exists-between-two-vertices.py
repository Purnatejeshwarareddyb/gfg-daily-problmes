class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        visited = [False] * len(adj)
        stack = [u]
        visited[u] = True
        while stack:
            curr = stack.pop()
            if curr == v:
                return True
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)
        return False