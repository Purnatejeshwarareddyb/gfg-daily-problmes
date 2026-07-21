class Solution:
    def isCyclic(self, V, edges):
        # code hear
        
        adj = [[] for _ in range(V)]
        in_degree = [0] * V
        
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
            
        queue = [i for i in range(V) if in_degree[i] == 0]
        visited_count = 0
        
        while queue:
            u = queue.pop(0)
            visited_count += 1
            
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        return visited_count != V
