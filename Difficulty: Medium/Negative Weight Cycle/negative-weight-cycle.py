class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        dist = [float('inf')] * V
        dist[0] = 0

        for _ in range(V - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break

        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return True

        return False