class Solution:
    def isBipartite(self, V, edges):
        # code hear
        
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        color = [-1] * V
        
        def dfs(node, current_color):
            color[node] = current_color
            
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - current_color):
                        return False
                elif color[neighbor] == current_color:
                    return False
                    
            return True
            
        for i in range(V):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
                    
        return True
