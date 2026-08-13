class Solution:
    def maxDistance(self, V: int, src: int, edges: list[list[int]]) -> list[int]:
       # code hear
        adj = [[] for _ in range(V)]
        in_degree = [0] * V
        for u, v, w in edges:
            adj[u].append((v, w))
            in_degree[v] += 1
            
        queue = [i for i in range(V) if in_degree[i] == 0]
        head = 0
        topo_order = []
        
        while head < len(queue):
            u = queue[head]
            head += 1
            topo_order.append(u)
            for v, w in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        INT_MIN = -2147483648
        dist = [INT_MIN] * V
        dist[src] = 0
        
        for u in topo_order:
            if dist[u] != INT_MIN:
                for v, w in adj[u]:
                    if dist[u] + w > dist[v]:
                        dist[v] = dist[u] + w
                        
        return dist