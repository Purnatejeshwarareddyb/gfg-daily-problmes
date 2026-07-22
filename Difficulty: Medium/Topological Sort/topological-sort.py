class Solution:
    def topoSort(self, V, edges):
        # Code hear
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            
        visited = [False] * V
        stack = []
        
        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)
            
        for i in range(V):
            if not visited[i]:
                dfs(i)
        return stack[::-1]
