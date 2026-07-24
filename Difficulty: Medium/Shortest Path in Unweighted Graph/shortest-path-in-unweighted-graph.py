class Solution:
    def shortestPath(self, V, edges, src, dest):
        # code hear
        
        if src == dest:
            return 0
            
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * V
        queue = [(src, 0)]
        visited[src] = True
        
        head = 0
        while head < len(queue):
            node, dist = queue[head]
            head += 1
            
            if node == dest:
                return dist
                
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
                    
        return -1
