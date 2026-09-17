class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        # code here
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append((v, 0))
            adj[v].append((u, 1))

        dist = [float('inf')] * (n + 1)
        dist[src] = 0

        deque = [src]

        while deque:
            u = deque.pop(0)

            if u == dst:
                return dist[u]

            for v, weight in adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    if weight == 0:
                        deque.insert(0, v)
                    else:
                        deque.append(v)

        return dist[dst] if dist[dst] != float('inf') else -1