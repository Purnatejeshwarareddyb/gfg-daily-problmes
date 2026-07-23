from typing import List

class Solution:
    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        # code hear
        
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        visited = [False] * V
        topo_order = []
        
        def dfs(node):
            visited[node] = True
            for neighbor, _ in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            topo_order.append(node)
            
        for i in range(V):
            if not visited[i]:
                dfs(i)
                
        topo_order.reverse()
        
        dist = [float('inf')] * V
        dist[0] = 0
        
        for node in topo_order:
            if dist[node] != float('inf'):
                for neighbor, weight in adj[node]:
                    if dist[node] + weight < dist[neighbor]:
                        dist[neighbor] = dist[node] + weight
                        
        return [d if d != float('inf') else -1 for d in dist]
